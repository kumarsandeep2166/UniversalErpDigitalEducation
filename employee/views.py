from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
class EmployeeCreateView(CreateView):
    model=Employee
    form_class=EmployeeForm
    template_name='student/employeemanagement.html'

    def get_context_data(self,**kwargs):
        context=super(EmployeeCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        username = request.session['username']
        context={'form':EmployeeForm(),'username':username}
        return render(request,'student/employeemanagement.html',context)
    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST or None,request.FILES or None)
        username = request.session['username']
        if form.is_valid():
            form.save()
        return render(request,'student/employeemanagement.html',{'form':form, 'username':username})


class EmployeeListView(ListView):
    model=Employee
    template_name='student/employee_list.html'
    queryset=Employee.objects.all()
    ordering=('-id')

    def get_context_data(self, *args ,**kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)    
        context['username'] = self.request.session['username']   
        return context 

class EmployeeDetailView(DetailView):
    context_object_name='employee_list'
    template_name='student/employee_detail.html'
    queryset = Employee.objects.all()
    
    def get_context_data(self, *args,**kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context['username'] = self.request.session['username']     
        return context
    
class EmployeeUpdateView(UpdateView):
    model=Employee
    fields='__all__'
    template_name='student/employeemanagement.html'
    success_url=reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model=Employee
    success_url=reverse_lazy('employee_list')