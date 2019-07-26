from django.shortcuts import render,redirect
from .models import FeesPlanType,ApproveFeeplanType, Note, FeeCollect
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView,View
from .forms import FeesPlanTypeForm
from coursemanagement.models import Stream, Course, Batch
from django.db.models import Q
from student.models import Enrollment, Student
from coursemanagement.models import Course, Batch, Stream
import datetime
import calendar
from django.http import HttpResponse
from django.contrib.auth.models import User

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

class FeesPlanTypeCreate(CreateView):
    model=FeesPlanType
    form_class=FeesPlanTypeForm
    template_name='feeplan/feeplan_create.html'

    def get(self, request, *args, **kwargs):
        username = request.session['username']
        context={'form':FeesPlanTypeForm(),'username':username}
        return render(request, 'feeplan/feeplan_create.html', context)

    def post(self, request, *args, **kwargs):
        username = request.session['username']
        form=FeesPlanTypeForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                form.save()
                return redirect("feeplan_list")
        return render(request, 'feeplan/feeplan_create.html', {'form':form,'username':username})

class FeesPlanTypeView(ListView):
    model=FeesPlanType
    template_name='feeplan/feeplan_list.html'
    context_object_name='object'
    stream_object=Stream.objects.all()
    course_object=Course.objects.all()
    batch_obj=Batch.objects.all()

    def get_context_data(self, *args, **kwargs):        
        context = super().get_context_data(**kwargs)
        context['stream_object'] = self.stream_object
        context['course_object'] = self.course_object
        context['batch_obj'] = self.batch_obj
        context['username'] = self.request.session['username']
        return context

def ajax_load_list_data(request):
    username = request.session['username']
    stream_id=request.GET.get('stream_id')
    course_id=request.GET.get('course_id')
    batch_id=request.GET.get('batch_id')
    print(stream_id, course_id, batch_id)
    objects=FeesPlanType.objects.filter(course=course_id,stream=stream_id,batch=batch_id)
    context={'objects': objects, 'username':username}
    return render(request,'feeplan/includes/data.html',context)
"""
feeplanType
stores information of current Course, Stream and Batch after submitting and the view shows
1. Fee type
2. Actual fees
3. No of Installments
"""
"""
ApproveFeePlanType
Stores information of a student by selecting enrollment number
1. Search the enrollment number then submit
2. Automatically select course and batch related to enrollment number
3. On approve section insert
        1. Enrollment Number
        2. course
        3. Batch
        4. Feetype
                1. Feetype
                2. Amount
                3. No. Of installments

        5. Aprrove Section in the same table 
                1. Approved Fees
                2. No of Installments
                    If installment is 1 then 1 pop up box will be opened and will ask for fees and date
                        1. Fees
                        2. Date
                    And so on for each no of installments but the maximum limit is 3
"""
class FeePlanCreate(View):    
    template_name='feeplan/feecollection.html'
    def get(self, request, id, *args, **kwargs):
        username = request.session['username']
        stud_obj = Student.objects.get(pk=id)
        course_name=stud_obj.course.course_name
        batch_no=stud_obj.batch.batch_no
        approved_fee_objs = ApproveFeeplanType.objects.filter(student=stud_obj)
        fee_list = []
        feetype_list = []
        if approved_fee_objs:
            for feeplan_obj in approved_fee_objs:
                feetype_dic = {}
                fee_list.append(feeplan_obj.fees_node.fees_type.pk)
                feetype_dic['fee_type_id'] = feeplan_obj.fees_node.pk
                feetype_dic['fee_type'] = feeplan_obj.fees_node.fees_type.fee_type
                feetype_dic['actual_fees'] = feeplan_obj.fees_node.actual_fees
                feetype_dic['default_installment'] = feeplan_obj.fees_node.default_installment
                feetype_dic['approved_amt'] = feeplan_obj.approve_fees
                feetype_dic['approved_installment'] = feeplan_obj.no_of_installments
                feetype_dic['first_installment_date'] = feeplan_obj.due_date_first_installment.strftime("%Y-%m-%d")
                feetype_dic['first_installment_amt'] = feeplan_obj.first_installment
                if feeplan_obj.second_installment is not None:
                    feetype_dic['sec_installment_date'] = feeplan_obj.due_date_second_installment.strftime("%Y-%m-%d")
                    feetype_dic['sec_installment_amt'] = feeplan_obj.second_installment
                if feeplan_obj.third_installment is not None:
                    feetype_dic['third_installment_date'] = feeplan_obj.due_date_third_installment.strftime("%Y-%m-%d")
                    feetype_dic['third_installment_amt'] = feeplan_obj.third_installment
                feetype_list.append(feetype_dic)
            print(fee_list)
        
        feeplan_objs = FeesPlanType.objects.filter(
            stream=stud_obj.stream,
            course=stud_obj.course,
            batch=stud_obj.batch).exclude(fees_type__in=fee_list)
        
        for feeplan_obj in feeplan_objs:
            feetype_dic = {}
            feetype_dic['fee_type_id'] = feeplan_obj.pk
            feetype_dic['fee_type'] = feeplan_obj.fees_type.fee_type
            feetype_dic['actual_fees'] = feeplan_obj.actual_fees
            feetype_dic['default_installment'] = feeplan_obj.default_installment
            feetype_list.append(feetype_dic)
        
        context={ 'stud_obj':stud_obj.pk,
                    'course_name':course_name,
                    'batch_no': batch_no,
                    'feetype_list':feetype_list,
                    'total':len(feetype_list),
                    'username': username}
        return render(request, 'feeplan/feecollection.html', context)

    def post(self, request, id, *args, **kwargs):
        counter = request.POST.get('total')
        username = request.session['username']
        stud_obj = Student.objects.get(pk=id)
        course_obj = stud_obj.course
        batch_obj = stud_obj.batch
        
        for i in range(int(counter)):
            try:        
                fee_type_id = request.POST.get('fee_type_id'+str(i))            
                fee_plan_obj = FeesPlanType.objects.get(pk=fee_type_id)
                try:
                    approved_installment = request.POST.get('approved_installment'+str(i))
                    approved_fee = float(request.POST.get('approved_fee'+str(i)))
                    total_installment = int(approved_installment)
                except:
                    approved_fee = 0
                    total_installment = 0
                appr_fee_plan_obj, created = ApproveFeeplanType.objects.get_or_create(
                    student=stud_obj,
                    fees_node=fee_plan_obj,
                    batch=batch_obj,
                    course=course_obj)
                appr_fee_plan_obj.approve_fees = approved_fee
                appr_fee_plan_obj.no_of_installments = total_installment
                somedate = datetime.date.today()
                if total_installment == 1:
                    first_amt =float( request.POST.get('first_installment_amt'+str(i)))
                    first_date =int( request.POST.get('first_installment_date'+str(i)))
                    appr_fee_plan_obj.first_installment = first_amt
                    appr_fee_plan_obj.due_date_first_installment = first_date
                elif total_installment == 2 :
                    first_amt =float( request.POST.get('first_installment_amt'+str(i)))
                    first_date =int( request.POST.get('first_installment_date'+str(i)))
                    sec_amt =float( request.POST.get('sec_installment_amt'+str(i)))
                    sec_date =int( request.POST.get('sec_installment_date'+str(i)))
                    appr_fee_plan_obj.first_installment = first_amt
                    appr_fee_plan_obj.second_installment = sec_amt
                    appr_fee_plan_obj.due_date_first_installment = first_date
                    appr_fee_plan_obj.due_date_second_installment = sec_date
                elif total_installment == 3:
                    first_amt =float( request.POST.get('first_installment_amt'+str(i)))
                    first_date =request.POST.get('first_installment_date'+str(i))
                    sec_amt =float( request.POST.get('sec_installment_amt'+str(i)))
                    sec_date =request.POST.get('sec_installment_date'+str(i))
                    third_amt =float( request.POST.get('third_installment_amt'+str(i)))
                    third_date =request.POST.get('third_installment_date'+str(i))
                    appr_fee_plan_obj.first_installment = first_amt
                    appr_fee_plan_obj.second_installment = sec_amt
                    appr_fee_plan_obj.third_installment = third_amt
                    appr_fee_plan_obj.due_date_first_installment = first_date
                    appr_fee_plan_obj.due_date_second_installment = sec_date
                    appr_fee_plan_obj.due_date_third_installment = third_date
                else:
                    default_installment = int(request.POST.get('default_installment'+str(i)))
                    default_fee = float(request.POST.get('default_fee'+str(i)))
                    today_date = datetime.date.today()
                    if default_installment==1:
                        appr_fee_plan_obj.first_installment = default_fee
                    elif default_installment==2:
                        default_fee = default_fee/2
                        first_date = today_date
                        sec_date = add_months(today_date, 6)
                        appr_fee_plan_obj.first_installment = default_fee
                        appr_fee_plan_obj.second_installment = default_fee
                        appr_fee_plan_obj.due_date_first_installment = first_date
                        appr_fee_plan_obj.due_date_second_installment = sec_date
                    elif default_installment==3:
                        default_fee = default_fee/3
                        first_date = today_date
                        sec_date = add_months(today_date, 4)
                        third_date = add_months(today_date, 4)
                        appr_fee_plan_obj.first_installment = default_fee
                        appr_fee_plan_obj.second_installment = default_fee
                        appr_fee_plan_obj.third_installment = default_fee
                        appr_fee_plan_obj.due_date_first_installment = first_date
                        appr_fee_plan_obj.due_date_second_installment = sec_date
                        appr_fee_plan_obj.due_date_third_installment = third_date
                appr_fee_plan_obj.save()
            except Exception as e:
                print(e)
        course_name=stud_obj.course.course_name
        batch_no=stud_obj.batch.batch_no
        approved_fee_objs = ApproveFeeplanType.objects.filter(student=stud_obj)
        fee_list = []
        feetype_list = []
        if approved_fee_objs:
            for feeplan_obj in approved_fee_objs:
                feetype_dic = {}
                fee_list.append(feeplan_obj.fees_node.fees_type.pk)
                feetype_dic['fee_type_id'] = feeplan_obj.fees_node.pk
                feetype_dic['fee_type'] = feeplan_obj.fees_node.fees_type.fee_type
                feetype_dic['actual_fees'] = feeplan_obj.fees_node.actual_fees
                feetype_dic['default_installment'] = feeplan_obj.fees_node.default_installment
                feetype_dic['approved_amt'] = feeplan_obj.approve_fees
                feetype_dic['approved_installment'] = feeplan_obj.no_of_installments
                feetype_dic['first_installment_date'] = feeplan_obj.due_date_first_installment.strftime("%Y-%m-%d")
                feetype_dic['first_installment_amt'] = feeplan_obj.first_installment
                if feeplan_obj.second_installment is not None:
                    feetype_dic['sec_installment_date'] = feeplan_obj.due_date_second_installment.strftime("%Y-%m-%d")
                    feetype_dic['sec_installment_amt'] = feeplan_obj.second_installment
                if feeplan_obj.third_installment is not None:
                    feetype_dic['third_installment_date'] = feeplan_obj.due_date_third_installment.strftime("%Y-%m-%d")
                    feetype_dic['third_installment_amt'] = feeplan_obj.third_installment
                feetype_list.append(feetype_dic)
            print(fee_list)
        
        feeplan_objs = FeesPlanType.objects.filter(
            stream=stud_obj.stream,
            course=stud_obj.course,
            batch=stud_obj.batch).exclude(fees_type__in=fee_list)
        
        for feeplan_obj in feeplan_objs:
            feetype_dic = {}
            feetype_dic['fee_type_id'] = feeplan_obj.pk
            feetype_dic['fee_type'] = feeplan_obj.fees_type.fee_type
            feetype_dic['actual_fees'] = feeplan_obj.actual_fees
            feetype_dic['default_installment'] = feeplan_obj.default_installment
            feetype_list.append(feetype_dic)
        
        context={ 'stud_obj':stud_obj.pk,
                    'course_name':course_name,
                    'batch_no': batch_no,
                    'feetype_list':feetype_list,
                    'total':len(feetype_list),
                    'username':username}
        
        return render(request, 'feeplan/feecollection.html', context)

def add_note(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        note = request.POST.get('note')
        note_type = request.POST.get('note_type')
        username = request.session['username']
        user_obj = User.objects.get(username=username)
        student_obj = Student.objects.get(pk=student_id)
        note_obj = Note()
        note_obj.student_admission_id = student_obj
        note_obj.note = note
        note_obj.user_id = user_obj
        note_obj.note_type = note_type
        note_obj.save()
        print(note_obj.pk)
    else:
        student_id = request.GET.get('student_id')
        note_type = request.GET.get('note_type')
        username = request.session['username']
    note_objs = Note.objects.filter(
        student_admission_id=student_id,
        note_type=note_type,
        is_active=1).order_by('-is_pin', '-pk')
    note_list = []
    for note_ob in note_objs:
        note_dic ={}
        note_dic['note'] = note_ob.note
        if note_ob.is_pin:
            note_dic['is_pin'] = note_ob.is_pin
        else:
            note_dic['is_pin'] = ''
        note_dic['username'] = username
        note_dic['note_id'] = note_ob.pk
        note_list.append(note_dic) 
    
    context={'note_list': note_list}
    return render(request,'feeplan/includes/note.html',context)


def pin_toggle_note(request):
    note_id = request.GET.get('note_id')
    student_id = request.GET.get('student_id')
    note_obj = Note.objects.get(pk=note_id)
    note_type = request.GET.get('note_type')
    username = request.session['username']
    if note_obj.is_pin:
        note_obj.is_pin = False
    else:
        note_obj.is_pin = True
    note_obj.save()
    note_objs = Note.objects.filter(
        student_admission_id=student_id,
        note_type=note_type,
        is_active=1).order_by('-is_pin', '-pk')
    note_list = []
    for note_ob in note_objs:
        note_dic ={}
        note_dic['note'] = note_ob.note
        if note_ob.is_pin:
            note_dic['is_pin'] = note_ob.is_pin
        else:
            note_dic['is_pin'] = ''
        note_dic['username'] = username
        note_dic['note_id'] = note_ob.pk
        note_list.append(note_dic)
    
    context={'note_list': note_list}
    return render(request,'feeplan/includes/note.html',context)


class FeePlanApprove(View):    
    template_name='feeplan/feecollection.html'
    def get(self, request, id, *args, **kwargs):
        username = request.session['username']
        stud_obj = Student.objects.get(pk=id)
        approved = stud_obj.fee_status
        course_name=stud_obj.course.course_name
        batch_no=stud_obj.batch.batch_no
        approved_fee_objs = ApproveFeeplanType.objects.filter(student=stud_obj)
        feetype_list = []
        if approved_fee_objs:
            for feeplan_obj in approved_fee_objs:
                feetype_dic = {}
                feetype_dic['fee_type_id'] = feeplan_obj.fees_node.pk
                feetype_dic['fee_type'] = feeplan_obj.fees_node.fees_type.fee_type
                feetype_dic['actual_fees'] = feeplan_obj.fees_node.actual_fees
                feetype_dic['default_installment'] = feeplan_obj.fees_node.default_installment
                feetype_dic['approved_amt'] = feeplan_obj.approve_fees
                feetype_dic['approved_installment'] = feeplan_obj.no_of_installments
                feetype_dic['first_installment_date'] = feeplan_obj.due_date_first_installment.strftime("%Y-%m-%d")
                feetype_dic['first_installment_amt'] = feeplan_obj.first_installment
                if feeplan_obj.second_installment is not None:
                    feetype_dic['sec_installment_date'] = feeplan_obj.due_date_second_installment.strftime("%Y-%m-%d")
                    feetype_dic['sec_installment_amt'] = feeplan_obj.second_installment
                if feeplan_obj.third_installment is not None:
                    feetype_dic['third_installment_date'] = feeplan_obj.due_date_third_installment.strftime("%Y-%m-%d")
                    feetype_dic['third_installment_amt'] = feeplan_obj.third_installment
                   
               
                feetype_list.append(feetype_dic)
        print(feetype_list)
        context={ 'stud_obj':stud_obj.pk,
                    'course_name':course_name,
                    'batch_no': batch_no,
                    'feetype_list':feetype_list,
                    'total':len(feetype_list),
                    'username': username,
                    'approved': approved}
        return render(request, 'feeplan/approvecollection.html', context)

    def post(self, request, id, *args, **kwargs):
        counter = request.POST.get('total')
        username = request.session['username']
        stud_obj = Student.objects.get(pk=id)
        course_obj = stud_obj.course
        batch_obj = stud_obj.batch
        
        for i in range(int(counter)):
            try:        
                fee_type_id = request.POST.get('fee_type_id'+str(i))            
                fee_plan_obj = FeesPlanType.objects.get(pk=fee_type_id)
                approved_installment = request.POST.get('approved_installment'+str(i))
                approved_fee = float(request.POST.get('approved_fee'+str(i)))
                total_installment = int(approved_installment)
                appr_fee_plan_obj, created = ApproveFeeplanType.objects.get_or_create(
                    student=stud_obj,
                    fees_node=fee_plan_obj,
                    batch=batch_obj,
                    course=course_obj)
                appr_fee_plan_obj.approve_fees = approved_fee
                appr_fee_plan_obj.no_of_installments = total_installment
                somedate = datetime.date.today()
                print("here")
                if total_installment == 1:
                    first_amt =float( request.POST.get('first_installment_amt'+str(i)))
                    first_date =request.POST.get('first_installment_date'+str(i))
                    appr_fee_plan_obj.first_installment = first_amt
                    appr_fee_plan_obj.due_date_first_installment = first_date
                elif total_installment == 2 :
                    first_amt =float( request.POST.get('first_installment_amt'+str(i)))
                    first_date =request.POST.get('first_installment_date'+str(i))
                    sec_amt =float( request.POST.get('sec_installment_amt'+str(i)))
                    sec_date =request.POST.get('sec_installment_date'+str(i))
                    appr_fee_plan_obj.first_installment = first_amt
                    appr_fee_plan_obj.second_installment = sec_amt
                    appr_fee_plan_obj.due_date_first_installment = first_date
                    appr_fee_plan_obj.due_date_second_installment = sec_date
                elif total_installment == 3:
                    first_amt =float( request.POST.get('first_installment_amt'+str(i)))
                    first_date =request.POST.get('first_installment_date'+str(i))
                    sec_amt =float( request.POST.get('sec_installment_amt'+str(i)))
                    sec_date =request.POST.get('sec_installment_date'+str(i))
                    third_amt =float( request.POST.get('third_installment_amt'+str(i)))
                    third_date =request.POST.get('third_installment_date'+str(i))
                    appr_fee_plan_obj.first_installment = first_amt
                    appr_fee_plan_obj.second_installment = sec_amt
                    appr_fee_plan_obj.third_installment = third_amt
                    appr_fee_plan_obj.due_date_first_installment = first_date
                    appr_fee_plan_obj.due_date_second_installment = sec_date
                    appr_fee_plan_obj.due_date_third_installment = third_date
                appr_fee_plan_obj.save()
            except Exception as e:
                print(e)
        course_name=stud_obj.course.course_name
        batch_no=stud_obj.batch.batch_no
        stud_obj.fee_status=2
        stud_obj.save()
        approved_fee_objs = ApproveFeeplanType.objects.filter(student=stud_obj)
        approved = stud_obj.fee_status
        feetype_list = []
        if approved_fee_objs:
            for feeplan_obj in approved_fee_objs:
                feetype_dic = {}
                feetype_dic['fee_type_id'] = feeplan_obj.fees_node.pk
                feetype_dic['fee_type'] = feeplan_obj.fees_node.fees_type.fee_type
                feetype_dic['actual_fees'] = feeplan_obj.fees_node.actual_fees
                feetype_dic['default_installment'] = feeplan_obj.fees_node.default_installment
                feetype_dic['approved_amt'] = feeplan_obj.approve_fees
                feetype_dic['approved_installment'] = feeplan_obj.no_of_installments
                feetype_dic['first_installment_date'] = feeplan_obj.due_date_first_installment.strftime("%Y-%m-%d")
                feetype_dic['first_installment_amt'] = feeplan_obj.first_installment
                if feeplan_obj.second_installment is not None:
                    feetype_dic['sec_installment_date'] = feeplan_obj.due_date_second_installment.strftime("%Y-%m-%d")
                    feetype_dic['sec_installment_amt'] = feeplan_obj.second_installment
                if feeplan_obj.third_installment is not None:
                    feetype_dic['third_installment_date'] = feeplan_obj.due_date_third_installment.strftime("%Y-%m-%d")
                    feetype_dic['third_installment_amt'] = feeplan_obj.third_installment

                feetype_list.append(feetype_dic)
        
        context={ 'stud_obj':stud_obj.pk,
                    'course_name':course_name,
                    'batch_no': batch_no,
                    'feetype_list':feetype_list,
                    'total':len(feetype_list),
                    'username':username,
                    'approved': approved}
        
        return render(request, 'feeplan/approvecollection.html', context)


class CollectFee(View):
    def get(self, request, id, *args, **kwargs):
        try:
            enr_obj = Enrollment.objects.get(student_name=id)
        except:
            enr_obj = ""
        if enr_obj:
            approved_fee_objs = FeeCollect.objects.filter(student=id)
            approved_fee_list = []
            for approved_fee_obj in approved_fee_objs:
                approved_fee_dict = {}
                approved_fee_dict['fee_type'] = approved_fee_obj.approve_fee.fees_node.fees_type.fee_type
                approved_fee_dict['fee_type_id'] = approved_fee_obj.approve_fee.pk
                approved_fee_dict['fee_amount'] = approved_fee_obj.approve_fee.first_installment
                approved_fee_dict['amount_paid'] = approved_fee_obj.amount_paid
                approved_fee_dict['amount_left'] = approved_fee_obj.amount_left
                approved_fee_list.append(approved_fee_dict)
        else:
            approved_fee_objs = ApproveFeeplanType.objects.filter(student=id)
            approved_fee_list = []
            for approved_fee_obj in approved_fee_objs:
                approved_fee_dict = {}
                approved_fee_dict['fee_type'] = approved_fee_obj.fees_node.fees_type.fee_type
                approved_fee_dict['fee_type_id'] = approved_fee_obj.pk
                approved_fee_dict['fee_amount'] = approved_fee_obj.first_installment
                approved_fee_dict['amount_paid'] = 0
                approved_fee_dict['amount_left'] = approved_fee_obj.first_installment
                approved_fee_list.append(approved_fee_dict)
        context = {"object_list": approved_fee_list,
                    "total_fee_type": len(approved_fee_list),
                    "student_id": id}
        return render(request, 'student/fee_view.html', context)


def collectfeesave(request):
    student_id = request.POST.get('student_id')
    total_count = request.POST.get('total_fee_type')
    for i in range(int(total_count)):
        try:
            amount = float(request.POST.get('fee'+str(i)))
        except:
            amount = 0.0
        if amount > 0:
            enroll = True
            break
    if enroll:
        for i in range(int(total_count)):
            approve_id = request.POST.get('approve_fee_id'+str(i))
            approved_fee_obj = ApproveFeeplanType.objects.get(pk=approve_id)
            total_amount = float(approved_fee_obj.first_installment)
            try:
                amount = float(request.POST.get('fee'+str(i)))
            except:
                amount = 0.0
            if total_amount == amount:
                remaing_amt = 0.0
            else:
                remaing_amt = total_amount
            fee_collect_obj, created = FeeCollect.objects.get_or_create(
                student=approved_fee_obj.student,
                approve_fee=approved_fee_obj)
            fee_collect_obj.amount_paid = amount
            fee_collect_obj.amount_left = remaing_amt
            fee_collect_obj.save()
    
        stud_obj = approved_fee_obj.student
        stream_obj = approved_fee_obj.student.stream
        course_obj = approved_fee_obj.student.course
        batch_obj = approved_fee_obj.student.batch
        try:
            enrobj = Enrollment.objects.get(student_name=stud_obj)
        except:
            enrobj = ""
        if not enrobj:
            enrl_obj = Enrollment.objects.filter(stream=stream_obj, course=course_obj, batch=batch_obj).order_by('-pk')
            
            try:
                enrl_no = enrl_obj[0].enrollment_number
                enr_arr = enrl_no.split('/')
                enrl_no = int(enr_arr[-1])
                enrl_no += 1
                enrl_no = str(enrl_no)
                stream_abb = enr_arr[0]
                course_abb = enr_arr[1]
                batch_abb = enr_arr[2]
                sr_num = enrl_no.zfill(5)
                enrl_no = stream_abb + "/" + course_abb + "/" + batch_abb + "/" + sr_num
                enrl_obj = Enrollment.objects.create(stream=stream_obj, course=course_obj, batch=batch_obj, student_name=student_obj)
                enrl_obj.enrollment_number = enrl_no
                enrl_obj.save()
            except:
                enrl_obj = Enrollment.objects.create(stream=stream_obj, course=course_obj, batch=batch_obj, student_name=stud_obj)
                stream_abb = stream_obj.short_name
                course_abb = course_obj.course_aliases
                batch_abb = batch_obj.batch_no
                sr_num = '00001'
                enrl_no = stream_abb + "/" + course_abb + "/" + batch_abb + "/" + sr_num
                enrl_obj.enrollment_number = enrl_no
                enrl_obj.save()
    else:
        pass
    return redirect('/fee/collect_fee/'+student_id+"/")