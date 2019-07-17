from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
#from django.views.generic.edit import FormView
from .models import (Student,StudentEnquiry,Employee,Branch,Department,Enrollment)
from .forms import (StudentForm,StudentEnquiryForm,EmployeeForm,EnrollmentForm)
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from django.views.generic.base import TemplateView
from django.db.models import Q,Count

def index(request):    
    return render(request,'student/index.html')

def admissionfrm(request):
    return render(request,'student/admissionfrm.html',{})


def applicantfrm(request):
    form=StudentEnquiryForm()
    if request.method=="POST":
        form=StudentEnquiryForm(request.POST or None)
        if form.is_valid():
            form.save()
            #return redirect('admissionfrm')
        return render(request,'student/applicantfrm.html',{'form':form})

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
        return render(request,'student/applicantfrm.html',{'form':form})
def studentadmissionlist(request):
    return render(request,'student/studentadmissionlist.html',{})


def load_branches(request):
    department_id=request.GET.get('department')
    branches=Branch.objects.filter(department_id=department_id).order_by('branch')
    return render(request,'student/department_options.html',{'branches':branches})
   
class StudentCreateView(CreateView):
    model=Student
    form_class=StudentForm
    template_name='student/studentadmissionform.html'

    def get_context_data(self,**kwargs):
        context=super(StudentCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        context={'form':StudentForm(),}
        return render(request,'student/studentadmissionform.html',context)
    def post(self,request,*args,**kwargs):
        form=StudentForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            #return redirect('student_list')
        return render(request,'student/studentadmissionform.html',{'form':form})

class StudentListView(ListView):
    context_object_name='student_list'
    template_name='student/student_list.html'
    queryset=Student.objects.all()
    ordering=('-id')

    def get_context_data(self,**kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)       
        return context       

class StudentDetailView(DetailView):
    context_object_name='student_list'
    template_name='student/admissionfrm.html'
    queryset=Student.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)       
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

    def get_context_data(self,**kwargs):
        context = super(EnquiryListView, self).get_context_data(**kwargs)       
        return context

def is_valid_queryparam(param):
    return param != '' and param is not None

def search_list(request):
    qs=Student.objects.all()
    exact_search=request.GET.get('anything')
    category_search=request.GET.get('category')
    pass


class EmployeeCreateView(CreateView):
    model=Employee
    form_class=EmployeeForm
    template_name='student/employeemanagement.html'

    def get_context_data(self,**kwargs):
        context=super(EmployeeCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        context={'form':EmployeeForm(),}
        return render(request,'student/employeemanagement.html',context)
    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request,'student/employeemanagement.html',{'form':form})


class EmployeeListView(ListView):
    model=Employee
    template_name='student/employee_list.html'
    queryset=Employee.objects.all()
    ordering=('-id')

    def get_context_data(self,**kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)       
        return context 

class EmployeeDetailView(DetailView):
    context_object_name='employee_list'
    template_name='student/employee_detail.html'
    queryset=Employee.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)       
        return context
    
class EmployeeUpdateView(UpdateView):
    model=Employee
    fields='__all__'
    template_name='student/employeemanagement.html'
    success_url=reverse_lazy('employee_list')
class EmployeeDeleteView(DeleteView):
    model=Employee
    success_url=reverse_lazy('employee_list')

class EnorllmentView(CreateView):
    model=Enrollment
    fields=('course','stream','batch','enrollment_number','date_of_admission','student_name')
    template_name='student/enroll_student.html'
    success_url=reverse_lazy('student_list')
class EnrollmnetViewList(ListView):
    model=Enrollment
    template_name='student/enrollment_list.html'
    queryset=Enrollment.objects.all()
    ordering=('-id')

    def get_context_data(self,**kwargs):
        context = super(EnrollmnetViewList, self).get_context_data(**kwargs)       
        return context
class EnrollmnetViewDetail(DetailView):
    model=Enrollment
    template_name='student/enrollment_list.html'
    queryset=Enrollment.objects.all()
    

    def get_context_data(self,**kwargs):
        context = super(EnrollmnetViewDetail, self).get_context_data(**kwargs)       
        return context