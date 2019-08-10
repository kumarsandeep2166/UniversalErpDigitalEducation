from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, View
from .models import Semestar, Subject, SubjectTeacher, LessonPlan, Attendance, Section, SubjectProgerssReport, StudentSection
from .forms import SemestarForm, SubjectForm, SubjectTeacherForm, LessonPlanForm, AttendanceForm, StudentSectionForm,ClassTimingsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy,reverse
from employee.models import Employee, Category, Designation
from django.db import transaction
from django.db.models import Count
from student.models import Student
from django.db import connection
import json
from coursemanagement.models import Stream
import datetime


class SemestarCreateView(CreateView):
    model=Semestar
    form_class=SemestarForm
    template_name='academics/add_semestar.html'

    def get_context_data(self, **kwargs):
        context = super(SemestarCreateView,self).get_context_data(**kwargs)        
        return context
    def get(self,request,*args,**kwargs):
        context={'form':SemestarForm(),}
        return render(request,'academics/add_semestar.html',context)
    def post(self,request,*args,**kwargs):
        form=SemestarForm(request.POST or None)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse_lazy)
        return redirect('/semestar/')


class SemestarList(ListView):
    template_name='academics/semestar.html'
    context_object_name='semestar'
    queryset=Semestar.objects.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context


class SubjectCreateView(CreateView):
    model=Subject
    form_class=SubjectForm
    template_name='academics/add_subject.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectCreateView,self).get_context_data(**kwargs)        
        return context
    def get(self,request,*args,**kwargs):
        context={'form':SubjectForm(),}
        return render(request,'academics/add_subject.html',context)
    def post(self,request,*args,**kwargs):
        form=SubjectForm(request.POST or None)
        print(form)
        if form.is_valid():
            obj = form.save()
            print(obj)
        else:
            print("invalide form")
        return redirect('/subject/')


class SubjectList(ListView):
    template_name='academics/subject.html'
    context_object_name='subject'
    queryset=Subject.objects.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context


class SubjectTeacherCreateView(CreateView):
    model=SubjectTeacher
    form_class=SubjectTeacherForm
    template_name='academics/add_subject_teacher.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectTeacherCreateView,self).get_context_data(**kwargs)        
        return context
    def get(self,request,*args,**kwargs):
        context={'form':SubjectTeacherForm(),}
        print(context)
        return render(request,'academics/add_subject_teacher.html',context)
    def post(self,request,*args,**kwargs):
        form=SubjectTeacherForm(request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            print("saved")
        else:
            print(form.errors)
            #return HttpResponseRedirect(reverse_lazy)
        return redirect('/subject_teacher/')

def ajax_load_sem(request):
    batch_id=request.GET.get('batch_id')
    course=request.GET.get('course')
    stream_id=request.GET.get('stream_id')
    semestar=Semestar.objects.filter(stream=stream_id, course=course, batch=batch_id)
    context={'semestar':semestar}
    return render(request,'academics/semester_ajax_load.html',context)

def ajax_load_subject(request):
    semestar_id = request.GET.get('semestar_id')
    semestar = Semestar.objects.get(pk=semestar_id)
    subject = Subject.objects.filter(semestar=semestar)
    context={'subject':subject}
    return render(request,'academics/subject_ajax_load.html',context)

class SubjectTeacherList(ListView):
    template_name='academics/subject_teacher.html'
    context_object_name='subject_teacher'
    queryset=SubjectTeacher.objects.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class StudentTeacherUpdateView(UpdateView):
    model = SubjectTeacher
    form_class = SubjectTeacherForm    
    template_name = 'academics/studentteacher_update.html'
    success_url = reverse_lazy('subject_teacher-list')
       
    def post(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(SubjectTeacher, pk=pk)
        print(instance)
        form = SubjectTeacherForm(request.POST or None, instance=instance)
        print(pk)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('subject_teacher-list'))


class StudentTeacherDeleteView(DeleteView):
    model = SubjectTeacher
    success_url = reverse_lazy('subject_teacher-list')


# class LessonPlanCreateView(CreateView):
#     model = LessonPlan
#     form_class = LessonPlanForm
#     template_name = 'academics/add_lesson_plan.html'

#     def get_context_data(self, **kwargs):
#         data = super(LessonPlanCreateView,self).get_context_data(**kwargs)        
#         if self.request.POST:
#             data['titles'] = CollectionTitleFormSet(self.request.POST)
#         else:
#             data['titles'] = CollectionTitleFormSet()
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         titles = context['titles']
#         with transaction.atomic():
#             form.instance.created_by = self.request.user
#             self.object = form.save()
#             if titles.is_valid():
#                 titles.instance = self.object
#                 titles.save()
#         return super(LessonPlanCreateView, self).form_valid(form)
    

# def ajax_load_lesson(request):
#     form = LessonPlanForm()    
#     return render(request, 'academics/lesson_ajax.html',{'form':form})

def attendance(request):
    form = AttendanceForm()
    return render(request, 'academics/attendance_student.html', {'form':form})

def ajax_load_attendance(request):
    # batch_id=request.GET.get('batch_id')
    # course=request.GET.get('course')
    # stream_id=request.GET.get('stream_id')
    # semestar=Semestar.objects.filter(stream=stream_id, course=course, batch=batch_id)
    # subject = Subject.objects.filter(semestar=semestar)
    subject_id = request.GET.get('subject_id')
    section_id = request.GET.get('section_id')
    query = """	select
	stud.id, enr.enrollment_number, stud.first_name, stud.last_name,
	subtea.total_class_held, COUNT(att.student_id)
	FROM
	student_student as stud
	join student_enrollment as enr on stud.id = enr.student_name_id
	join academics_semestar as sem on stud.stream_id = sem.stream_id
	and stud.course_id = sem.course_id
	and stud.batch_id = sem.batch_id
	join academics_subject sub on sem.id = sub.semestar_id and sub.id = {0}
	join academics_section sec on sem.id = sec.semestar_id and sec.id={1}
	join academics_subjectteacher subtea on sub.id = subtea.subject_id and sec.id=subtea.section_id
	left join academics_attendance as att on subtea.id = att.subject_teacher_id
	and stud.id = att.student_id and att.attendance_type="P"
	GROUP BY
	att.subject_teacher_id,
	att.student_id;""".format(subject_id, section_id)
    cursor = connection.cursor()
    print(query)
    cursor.execute(query)
    query_list = cursor.fetchall()
    attendance_list = []
    for obj in query_list:
        attendance_dic = {}
        attendance_dic['stud_id'] = obj[0]
        attendance_dic['enr_no'] = obj[1]
        attendance_dic['name'] = obj[2] + " " + obj[3]
        class_held = int(obj[4])
        class_present = int(obj[5])
        attendance_dic['total_class'] = class_held
        attendance_dic['class_present'] = class_present
        attendance_dic['class_absent'] = class_held - class_present
        attendance_list.append(attendance_dic)
    attendance_json = json.dumps({'attendance_list': attendance_list})
    return HttpResponse(attendance_json, 'application/json')


def save_attendance(request):
    try:
        stud_count = int(request.POST.get('stud_count'))
        id_subject = request.POST.get('id_subject')
        id_section = request.POST.get('id_section')
        attendancedate = request.POST.get('attendancedate')
        from_datetime = request.POST.get('from_datetime')
        to_datetime = request.POST.get('to_datetime')
        from_datetime = attendancedate +" " + from_datetime 
        to_datetime = attendancedate + " " +to_datetime
        print(from_datetime)
        print(to_datetime)
        attendancedate = datetime.datetime.strptime(attendancedate, '%Y-%m-%d').date()
        from_datetime = datetime.datetime.strptime(from_datetime, '%Y-%m-%d %H:%M')
        to_datetime = datetime.datetime.strptime(to_datetime, '%Y-%m-%d %H:%M')
        remark = request.POST.get('remark')
        topic = request.POST.get('topic')
        duration = to_datetime - from_datetime
        duration = duration.total_seconds() / 3600
        if duration>0:
            sub_obj = SubjectTeacher.objects.get(subject=id_subject, section=id_section)
            at_objs = Attendance.objects.values_list('pk').filter(subject_teacher=sub_obj.pk, date=attendancedate)
            if len(list(at_objs))>0:
                attendance_json = json.dumps({'msg': "attendance on this date has been already done!!"})
                return HttpResponse(attendance_json, 'application/json')
            progress_obj = SubjectProgerssReport()
            progress_obj.from_datetime = from_datetime
            progress_obj.to_datetime = to_datetime
            progress_obj.duration = duration
            progress_obj.remark = remark
            progress_obj.topic = topic
            progress_obj.report = sub_obj
            progress_obj.save()

            total_class = int(sub_obj.total_class_held)
            sub_obj.total_class_held = total_class+1
            sub_obj.save()
            for i in range(stud_count):
                stud_id = request.POST.get('attn_list['+ str(i) +'][id]')
                attn_type = request.POST.get('attn_list['+ str(i) +'][attn]')
                remark = request.POST.get('attn_list['+ str(i) +'][remark]')
                att_obj = Attendance()
                att_obj.subject_teacher = sub_obj
                att_obj.student = Student.objects.get(pk=stud_id)
                att_obj.attendance_type = attn_type
                att_obj.date=attendancedate
                att_obj.remark = remark
                att_obj.save()
            
            attendance_json = json.dumps({'msg': "success", "id_subject":id_subject, "id_section":id_section})
        else:
            attendance_json = json.dumps({'msg': "Please Enter Correct Time!!!!!"})
    except:
        attendance_json = json.dumps({'msg': "Something went Wrong!!!"})
    return HttpResponse(attendance_json, 'application/json')
def teacher_load(request):
    stream_id = request.GET.get('stream_id')
    cat_obj = Category.objects.get(name="Teaching")
    designation_list = Designation.objects.values_list('pk').filter(category=cat_obj.pk)
    empl_obj = Employee.objects.filter(stream=stream_id, employee_designation__in=list(designation_list))    
    return render(request,'academics/teacher_load.html',{'object':empl_obj})


def get_section_subject(request):
    semestar_id = request.GET.get('semestar_id')
    subject_objs = Subject.objects.filter(semestar=semestar_id)
    subject_list = []
    for obj in subject_objs:
        sub_dic = {}
        sub_dic['id'] = obj.pk
        sub_dic['name'] = obj.name
        subject_list.append(sub_dic)

    section_objs = Section.objects.filter(semestar=semestar_id)
    section_list = []
    for obj in section_objs:
        section_dic = {}
        section_dic['id'] = obj.pk
        section_dic['name'] = obj.section_name
        section_list.append(section_dic)

    json_obj = json.dumps({'subject_list': subject_list, "section_list": section_list})
    return HttpResponse(json_obj, 'application/json')

def attendanceProgressDetailView(request):
    section_id = request.GET.get('section_id')
    subject_id = request.GET.get('subject_id')
    teacher_id = request.GET.get('teacher_id')
    if teacher_id:
        sub_teacher_obj = SubjectTeacher.objects.get(subject=subject_id,section=section_id, teacher=teacher_id)
    else:
        sub_teacher_obj = SubjectTeacher.objects.values_list('pk').filter(subject=subject_id,section=section_id)
    objs = SubjectProgerssReport.objects.filter(report__in=list(sub_teacher_obj))
    context = {
        'section_id':section_id,
        'subject_id':subject_id,        
        'objs':objs,

    }
    return render(request,'academics/progress_report.html',context)

def studentsectioncreate(request):
    if request.method == "POST":
        stream = request.POST.get('stream')
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        semestar = request.POST.get('semestar')
        total_section = int(request.POST.get('total_section'))
        sem_obj = Semestar.objects.get(pk=semestar)
        if total_section>0:
            stud_list = list(Student.objects.values_list('pk',flat=True).filter(batch=batch))
            total = len(stud_list)
            loop_count = total/total_section
            start = 0
            end = loop_count
            for i in range(total_section):
                name = str(chr(65+i))
                sec_obj, created = Section.objects.get_or_create(section_name=name, semestar=sem_obj)
                for stud_obj in Student.objects.filter(batch=batch)[start:end]:
                    obj, created = StudentSection.objects.get_or_create(student=stud_obj, section = sec_obj)
                start = end
                end = end + loop_count
                if end>total:
                    end=total                
                return redirect('/student_section_list/')
        else:
            pass

    else:
        form = StudentSectionForm()
        context = {"form":form}
    return render(request, 'academics/add_student_section.html', context)

def studentsection(request):
    batch_id = request.GET.get('batch_id')
    obj = Student.objects.filter(batch=batch_id)
    total = len(obj)
    context={'total':total}
    return render(request, 'academics/student_section.html', context)

def student_section_list(request):
    objs = StudentSection.objects.all()
    context = {'objs':objs}
    return render(request,'academics/student_section_list.html', context)

def class_timing_setting(request):
    form=ClassTimingsForm()
    return render(request, 'academics/class_time_table_setting.html',{'form':form})