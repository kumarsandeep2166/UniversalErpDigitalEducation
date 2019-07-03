from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Course
from .forms import CourseForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
class CourseList(ListView):
    template_name='course/course_list.html'
    context_object_name='courses'
    queryset=Course.objects.all()

    # def get(self,request,*args,**kwargs):
    #     course=Course.objects.all()
    #     context={'course':course}
    #     return render(request,'course/course_list.html',context)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class CourseCreateView(CreateView):
    model=Course
    form_class=CourseForm
    template_name='course/course_form.html'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView,self).get_context_data(**kwargs)        
        return context
    def get(self,request,*args,**kwargs):
        context={'form':CourseForm(),}
        return render(request,'course/course_form.html',context)
    def post(self,request,*args,**kwargs):
        form=CourseForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse_lazy)
        return render(request,'course/course_form.html',{'form':form})

        
def course_detail(request,pk):
    course=get_object_or_404(Course,pk=pk)    
    return render(request,"course/course_detail.html",{'object':course})
    
class CourseUpdateView(UpdateView):
    model=Course
    fields='__all__'
    template_name='course/course_update.html'
    success_url=reverse_lazy('course_list')
    
class CourseDeleteView(DeleteView):
    model=Course
    success_url=reverse_lazy('course_list')
def batch(request):
    return render(request,'course/batch.html',{})
def section(request):
    return render(request,'course/section.html',{})
def course(request):
    return render(request,'course/course.html',{})
def stream(request):
    return render(request,'course/stream.html',{})