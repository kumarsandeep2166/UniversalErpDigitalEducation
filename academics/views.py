from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, View
from .models import Semestar, Subject, SubjectTeacher, LessonPlan, Attendance
from .forms import SemestarForm, SubjectForm, SubjectTeacherForm, LessonPlanForm, AttendanceForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy,reverse
from employee.models import Employee
from django.db import transaction
from django.db.models import Count
from student.models import Student
from django.db import connection
import json

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
    query = """select
        stud.id, enr.enrollment_number, stud.first_name, stud.last_name, 
        sub.total_class_held, COUNT(att.student_id)
        FROM
        student_student as stud
        join student_enrollment as enr on stud.id = enr.student_name_id
        join academics_semestar as sem on stud.stream_id = sem.stream_id
        and stud.course_id = sem.course_id
        and stud.batch_id = sem.batch_id
        join academics_subject sub on sem.id = sub.semestar_id
        left join academics_attendance as att on sub.id = att.subject_id
        and stud.id = att.student_id
        WHERE
        sub.id = {0} and att.attendance_type="P"
        GROUP BY
        att.subject_id,
        att.student_id;""".format(subject_id)
    cursor = connection.cursor()
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



