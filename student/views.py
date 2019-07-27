from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
#from django.views.generic.edit import FormView
from .models import (Student,StudentEnquiry,Employee,Branch,Department,Enrollment)
from .forms import (StudentForm,StudentEnquiryForm,EmployeeForm,EnrollmentForm)
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView,View
from django.views.generic.base import TemplateView
from django.db.models import Q,Count
from coursemanagement.models import Stream, Course, Batch, Section
from django.http import HttpResponse,HttpResponseRedirect
import json
from django.contrib.auth.decorators import login_required


def index(request):   
    username = request.session['username']
    return render(request,'student/index.html',{'username': username})

def admissionfrm(request):
    return render(request,'student/admissionfrm.html',{})


def applicantfrm(request):
    form=StudentEnquiryForm()
    username = request.session['username']
    if request.method=="POST":
        form=StudentEnquiryForm(request.POST or None)
        if form.is_valid():
            form.save()
            #return redirect('admissionfrm')
        return render(request,'student/applicantfrm.html',{'form':form, 'username': username})

    # if request.method=='POST':
    #     fname=request.POST.get('fname')
    #     mname=request.POST.get('mname')
    #     lname=request.POST.get('lname')
    #     dob=request.POST.get('dob')
    #     phone_no=request.POST.get('phone')
    #     email=request.POST.get('email')
    #     shift=request.POST.get('shift')
    #     last_education=request.POST.get('rqual')
    #     entrance=request.POST.get('ent')
    #     year=request.POST.get('year')
    #     score=request.POST.get('score')
    #     s=StudentEnquiry(first_name=fname,middle_name=mname,last_name=lname,date_of_birth=dob,phone_no=phone_no,
    #     email_id=email,shift=shift,last_education=last_education,entrance=entrance,year=year,score=score)
    #     s.save()
    #     return render(request,'student/applicantfrm.html')
        
    else:
        form=StudentEnquiryForm()
        return render(request,'student/applicantfrm.html',{'form':form, 'username': username})
def studentadmissionlist(request):
    return render(request,'student/studentadmissionlist.html',{})


def load_branches(request):
    username = request.session['username']
    stream_id=request.GET.get('department')
    branches=Course.objects.filter(stream=stream_id).order_by('course_name')
    return render(request,'student/department_options.html',{'branches':branches, 'username': username})
   
class StudentCreateView(CreateView):
    model=Student
    form_class=StudentForm
    template_name='student/studentadmissionform.html'

    def get_context_data(self,**kwargs):
        context=super(StudentCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        username = request.session['username']
        context={'form':StudentForm(), 'username': username}
        return render(request,'student/studentadmissionform.html',context)
    def post(self,request,*args,**kwargs):
        form=StudentForm(request.POST or None,request.FILES or None)
        username = request.session['username']
        if form.is_valid():
            stud_obj = form.save()
            print(stud_obj)
            print(stud_obj.pk)
            return redirect('student_list')
        return render(request,'student/studentadmissionform.html',{'form':form, 'username': username})

class StudentListView(ListView):
    context_object_name='student_list'
    template_name='student/student_list.html'
    queryset=Student.objects.all()
    ordering=('-id')
    

    def get_context_data(self, *args, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs) 
        context['username'] = self.request.session['username']      
        return context       

class StudentDetailView(DetailView):
    context_object_name='student_list'
    template_name='student/student_detail.html'
    queryset=Student.objects.all()
    
    def get_context_data(self, *args ,**kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['username'] = self.request.session['username']     
        return context
    
class StudentUpdateView(UpdateView):
    model=Student
    fields='__all__'
    template_name='student/studentadmissionform.html'
    success_url=reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('student_list')

class EnquiryListView(ListView):
    context_object_name='enquiry_list'
    template_name='student/enquiry_list.html'
    queryset=StudentEnquiry.objects.all()
    ordering=('-id')

    def get_context_data(self, *args ,**kwargs):
        context = super(EnquiryListView, self).get_context_data(**kwargs)
        context['username'] = self.request.session['username']   
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None

def search_list(request):
    qs=Student.objects.all()
    exact_search=request.GET.get('anything')
    category_search=request.GET.get('category')
    pass


# class EmployeeCreateView(CreateView):
#     model=Employee
#     form_class=EmployeeForm
#     template_name='student/employeemanagement.html'

#     def get_context_data(self,**kwargs):
#         context=super(EmployeeCreateView,self).get_context_data(**kwargs)
#         return context
#     def get(self,request,*args,**kwargs):
#         context={'form':EmployeeForm(),}
#         return render(request,'student/employeemanagement.html',context)
#     def post(self,request,*args,**kwargs):
#         form=EmployeeForm(request.POST or None,request.FILES or None)
#         if form.is_valid():
#             form.save()
#         return render(request,'student/employeemanagement.html',{'form':form})


# class EmployeeListView(ListView):
#     model=Employee
#     template_name='student/employee_list.html'
#     queryset=Employee.objects.all()
#     ordering=('-id')

#     def get_context_data(self,**kwargs):
#         context = super(EmployeeListView, self).get_context_data(**kwargs)       
#         return context 

# class EmployeeDetailView(DetailView):
#     context_object_name='employee_list'
#     template_name='student/employee_detail.html'
#     queryset=Employee.objects.all()
    
#     def get_context_data(self,**kwargs):
#         context = super(EmployeeDetailView, self).get_context_data(**kwargs)       
#         return context
    
# class EmployeeUpdateView(UpdateView):
#     model=Employee
#     fields='__all__'
#     template_name='student/employeemanagement.html'
#     success_url=reverse_lazy('employee_list')
# class EmployeeDeleteView(DeleteView):
#     model=Employee
#     success_url=reverse_lazy('employee_list')

class EnorllmentView(View):
    # model=Enrollment
    # form_class=EnrollmentForm    
    # template_name='student/enroll_student.html'      
    # context_object_name='student'

    def get(self, request,pk, *args, **kwargs):
        username = request.session['username']
        student_id = request.GET.get('pk')
        stuid_obj = Student.objects.get(pk=pk)
        try:
            enr_obj = Enrollment.objects.get(student_name=stuid_obj)
            enr_no = enr_obj.enrollment_number
        except:
            enr_no = ""
        name = stuid_obj.first_name + " " + stuid_obj.middle_name + " " + stuid_obj.last_name
        context={'form':EnrollmentForm(), 'name': name, "enr_no": enr_no, 'id': stuid_obj.pk, 'username':username}
        return render(request,'student/enroll_student.html',context)
    
    def post(self, request, *args, **kwargs):
        username = request.session['username']
        form=EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('student_list'))
        else:
            print(form)
        return render(request,'student/enroll_student.html',{'form':form, 'username':username})



class EnrollmnetViewList(ListView):
    model=Enrollment
    template_name='student/enrollment_list.html'
    queryset=Enrollment.objects.all()
    ordering=('-id')

    def get_context_data(self, *args ,**kwargs):
        context = super(EnrollmnetViewList, self).get_context_data(**kwargs)
        context['username'] = self.request.session['username']     
        return context


class EnrollmnetViewDetail(DetailView):
    model=Enrollment
    template_name='student/enrollment_list.html'
    queryset=Enrollment.objects.all()
    

    def get_context_data(self, *args ,**kwargs):
        context = super(EnrollmnetViewDetail, self).get_context_data(**kwargs)
        context['username'] = self.request.session['username']
        return context


def ajax_load_enrollment(request):
    username = request.session['username']
    stream_id=request.GET.get('stream_id')
    course_id=request.GET.get('course_id')
    batch_id=request.GET.get('batch_id')
    student_id = request.GET.get('student_id')
    student_obj = Student.objects.get(pk=student_id)
    stream_obj = Stream.objects.get(pk=stream_id)
    course_obj = Course.objects.get(pk=course_id)
    batch_obj = Batch.objects.get(pk=batch_id) 
    try:
        stud_obj = Enrollment.objects.get(student_name=student_obj)
        if stud_obj:
            context={'msg':"student already enrolled"}
            return HttpResponse(json.dumps(context), content_type="application/json")
    except:
        pass
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
        enrl_obj = Enrollment.objects.create(stream=stream_obj, course=course_obj, batch=batch_obj, student_name=student_obj)
        stream_abb = stream_obj.short_name
        course_abb = course_obj.course_aliases
        batch_abb = batch_obj.batch_no
        sr_num = '00001'
        enrl_no = stream_abb + "/" + course_abb + "/" + batch_abb + "/" + sr_num
        enrl_obj.enrollment_number = enrl_no
        enrl_obj.save()
    context={'section':enrl_no, 'msg': '' , 'username':username}
    return HttpResponse(json.dumps(context), content_type="application/json")


def start_admission(request, id):
    username = request.session['username']
    if request.method == "POST":
        pass
    else:
        stud_obj = StudentEnquiry.objects.get(pk=id)
        form = StudentForm()
        form.fields["first_name"].initial = stud_obj.first_name
        form.fields["middle_name"].initial = stud_obj.middle_name
        form.fields["last_name"].initial = stud_obj.last_name
        form.fields["date_of_birth"].initial = "2019-01-01"#stud_obj.date_of_birth
        form.fields["phone_number"].initial = stud_obj.phone_no
        form.fields["email"].initial = stud_obj.email_id
        form.fields["entrance_name"].initial = stud_obj.entrance
        form.fields["entrance_year"].initial = stud_obj.year
        form.fields["entrance_score"].initial = stud_obj.score

        return render(request,'student/studentadmissionform.html',{'form':form, 'username': username})


def approve_academic(request):
    student_id = request.POST.get('student_id')
    stud_obj = Student.objects.get(pk=student_id)
    stud_obj.academic_status=2
    stud_obj.save()
    context={'msg':"Approved"}
    return HttpResponse(json.dumps(context), content_type="application/json")

def reject_academic(request):
    student_id = request.POST.get('student_id')
    stud_obj = Student.objects.get(pk=student_id)
    stud_obj.academic_status=0
    stud_obj.save()
    context={'msg':"Rejected"}
    return HttpResponse(json.dumps(context), content_type="application/json")

class Enroll_StudentList(View):
    
    template_name = 'student/enroll_student_list.html'

    def get(self, request, *args, **kwargs):
        object_list = Student.objects.filter(academic_status=2, fee_status=2)
        print(object_list[0].academic_status)
        print(object_list[0].fee_status)
        return render(request, 'student/enroll_student_list.html', context={'object_list':object_list})
    
    