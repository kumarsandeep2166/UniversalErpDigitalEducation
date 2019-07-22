from django.shortcuts import render,redirect
from .models import FeesPlanType,ApproveFeeplanType
#from django.forms import modelformset_factory,inlineformset_factory
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView,View
from .forms import FeesPlanTypeForm
from coursemanagement.models import Stream, Course, Batch
from django.db.models import Q
from student.models import Enrollment, Student
from coursemanagement.models import Course, Batch, Stream

import datetime
import calendar

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)


# def index(request):
#     ExampleFormSet=modelformset_factory(FeesPlanType,fields=('stream','course','batch','fees_type','actual_fees',),extra=1)    
#     if request.method=="POST":        
#         form=ExampleFormSet(request.POST or None,request.FILES or None) 
#         if form.is_valid():       
#             instances=form.save(commit=False)
#             for instance in instances:
#                 instance.save()
#     else:
#         form=ExampleFormSet() 
#     return render(request,'feeplan/index.html',{'form':form})

# def homefee(request,fee_id):
#     fees_id=FeesPlanType.objects.get(pk=fee_id)
#     return render(request,'feeplan/index.html',{})

class FeesPlanTypeCreate(CreateView):
    model=FeesPlanType
    form_class=FeesPlanTypeForm
    template_name='feeplan/feeplan_create.html'

    def get(self, request, *args, **kwargs):
        context={'form':FeesPlanTypeForm()}
        return render(request, 'feeplan/feeplan_create.html', context)

    def post(self, request, *args, **kwargs):
        form=FeesPlanTypeForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                form.save()
                return redirect("feeplan_list")
        return render(request, 'feeplan/feeplan_create.html', {'form':form})


class FeesPlanTypeView(ListView):
    model=FeesPlanType
    template_name='feeplan/feeplan_list.html'
    context_object_name='object'
    stream_object=Stream.objects.all()
    course_object=Course.objects.all()
    batch_obj=Batch.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stream_object'] = self.stream_object
        context['course_object'] = self.course_object
        context['batch_obj'] = self.batch_obj

        return context


def ajax_load_list_data(request):
    stream_id=request.GET.get('stream_id')
    course_id=request.GET.get('course_id')
    batch_id=request.GET.get('batch_id')
    print(stream_id, course_id, batch_id)
    objects=FeesPlanType.objects.filter(course=course_id,stream=stream_id,batch=batch_id)
    context={'objects': objects}
    return render(request,'feeplan/includes/data.html',context)
    
def feecollection(request):
    enrollment_number=request.GET.get('enrollment_number')
    
    #qs=ApproveFeeplanType.objects.filter(enrollment_num=enrollment_number)
    qs=Enrollment.objects.filter(enrollment_number=enrollment_number)
    print(qs)
    course_obj=Course.objects.all()
    batch_obj=Batch.objects.all()
    print(course_obj)
    print(batch_obj)
    
    #print(qs)
    # stream_id=request.GET.get('stream_id')
    # course_id=request.GET.get('course_id')
    # batch_id=request.GET.get('batch_id')
    # print(stream_id, course_id, batch_id)
    

    try:
        pass
    except:
        pass
    return render(request,'feeplan/feecollection.html',{'qs':qs})

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

class ApproveFeePlanCreate(View):
    
    template_name='feeplan/feecollection.html'

    def get(self, request, id, *args, **kwargs):
        stuid_obj = Student.objects.get(pk=id)
        enr_obj = Enrollment.objects.get(student_name=stuid_obj)
        enr_no = enr_obj.enrollment_number
        course_name=enr_obj.course.course_name
        batch_no=enr_obj.batch.batch_no
        approved_fee_objs = ApproveFeeplanType.objects.filter(enrollment_num=enr_obj)
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
                feetype_dic['first_installment_date'] = feeplan_obj.due_date_first_installment.strftime("%m/%d/%Y")
                feetype_dic['first_installment_amt'] = feeplan_obj.first_installment
                if feeplan_obj.second_installment is not None:
                    feetype_dic['sec_installment_date'] = feeplan_obj.due_date_second_installment.strftime("%m/%d/%Y")
                    feetype_dic['sec_installment_amt'] = feeplan_obj.second_installment
                if feeplan_obj.third_installment is not None:
                    feetype_dic['third_installment_date'] = feeplan_obj.due_date_third_installment.strftime("%m/%d/%Y")
                    feetype_dic['third_installment_amt'] = feeplan_obj.third_installment
                feetype_list.append(feetype_dic)
            print(fee_list)
        
        feeplan_objs = FeesPlanType.objects.filter(
            stream=enr_obj.stream,
            course=enr_obj.course,
            batch=enr_obj.batch).exclude(fees_type__in=fee_list)
        
        for feeplan_obj in feeplan_objs:
            feetype_dic = {}
            feetype_dic['fee_type_id'] = feeplan_obj.pk
            feetype_dic['fee_type'] = feeplan_obj.fees_type.fee_type
            feetype_dic['actual_fees'] = feeplan_obj.actual_fees
            feetype_dic['default_installment'] = feeplan_obj.default_installment
            feetype_list.append(feetype_dic)
        print(feetype_list)
        context={ 'enr_no':enr_no,
                    'course_name':course_name,
                    'batch_no': batch_no,
                    'feetype_list':feetype_list,
                    'total':len(feetype_list)}
        return render(request, 'feeplan/feecollection.html', context)

    def post(self, request, id, *args, **kwargs):
        counter = request.POST.get('total')
         
        stuid_obj = Student.objects.get(pk=id)
        enr_obj = Enrollment.objects.get(student_name=stuid_obj)
        course_obj = enr_obj.course
        batch_obj = enr_obj.batch
        print(counter)
        for i in range(int(counter)):
            
            fee_type_id = request.POST.get('fee_type_id'+str(i))
            
           
            
            fee_plan_obj = FeesPlanType.objects.get(pk=fee_type_id)
            approved_installment = request.POST.get('approved_installment'+str(i))
            approved_fee = float(request.POST.get('approved_fee'+str(i)))
            total_installment = int(approved_installment)
            appr_fee_plan_obj, created = ApproveFeeplanType.objects.get_or_create(
                enrollment_num=enr_obj,
                fees_node=fee_plan_obj,
                batch=batch_obj,
                course=course_obj)
            appr_fee_plan_obj.approve_fees = approved_fee
            appr_fee_plan_obj.no_of_installments = total_installment
            somedate = datetime.date.today()
            if total_installment == 1:
                first_amt = approved_fee
                first_date = somedate
                appr_fee_plan_obj.first_installment = first_amt
                appr_fee_plan_obj.due_date_first_installment = first_date
            elif total_installment == 2 :
                first_amt = sec_amt = approved_fee/2
                first_date = somedate
                sec_date = add_months(somedate,6)
                first_amt = approved_fee/3
                first_date = somedate
                sec_date = add_months(somedate, 4)
                third_date = add_months(somedate, 4)
                appr_fee_plan_obj.first_installment = first_amt
                appr_fee_plan_obj.second_installment = first_amt
                appr_fee_plan_obj.due_date_first_installment = first_date
                appr_fee_plan_obj.due_date_second_installment = sec_date
            elif total_installment == 3:
                first_amt = approved_fee/3
                first_date = somedate
                sec_date = add_months(somedate, 4)
                third_date = add_months(somedate, 4)
                appr_fee_plan_obj.first_installment = first_amt
                appr_fee_plan_obj.second_installment = first_amt
                appr_fee_plan_obj.third_installment = first_amt
                appr_fee_plan_obj.due_date_first_installment = first_date
                appr_fee_plan_obj.due_date_second_installment = sec_date
                appr_fee_plan_obj.due_date_third_installment = third_date
            appr_fee_plan_obj.save()
        enr_no = enr_obj.enrollment_number
        course_name=enr_obj.course.course_name
        batch_no=enr_obj.batch.batch_no
        approved_fee_objs = ApproveFeeplanType.objects.filter(enrollment_num=enr_obj)
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
                feetype_dic['first_installment_date'] = feeplan_obj.due_date_first_installment.strftime("%m/%d/%Y")
                feetype_dic['first_installment_amt'] = feeplan_obj.first_installment
                if feeplan_obj.second_installment is not None:
                    feetype_dic['sec_installment_date'] = feeplan_obj.due_date_second_installment.strftime("%m/%d/%Y")
                    feetype_dic['sec_installment_amt'] = feeplan_obj.second_installment
                if feeplan_obj.third_installment is not None:
                    feetype_dic['third_installment_date'] = feeplan_obj.due_date_third_installment.strftime("%m/%d/%Y")
                    feetype_dic['third_installment_amt'] = feeplan_obj.third_installment
                feetype_list.append(feetype_dic)
            print(fee_list)
        
        feeplan_objs = FeesPlanType.objects.filter(
            stream=enr_obj.stream,
            course=enr_obj.course,
            batch=enr_obj.batch).exclude(fees_type__in=fee_list)
        
        for feeplan_obj in feeplan_objs:
            feetype_dic = {}
            feetype_dic['fee_type_id'] = feeplan_obj.pk
            feetype_dic['fee_type'] = feeplan_obj.fees_type.fee_type
            feetype_dic['actual_fees'] = feeplan_obj.actual_fees
            feetype_dic['default_installment'] = feeplan_obj.default_installment
            feetype_list.append(feetype_dic)
        print(feetype_list)
        context={ 'enr_no':enr_no,
                    'course_name':course_name,
                    'batch_no': batch_no,
                    'feetype_list':feetype_list,
                    'total':len(feetype_list)}
        if request.method=="POST":
            print(request)
        return render(request, 'feeplan/feecollection.html', context)

