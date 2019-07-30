from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView, View
from .models import Semestar, Subject, SubjectTeacher, LessonPlan
from .forms import SemestarForm, SubjectForm, SubjectTeacherForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from employee.models import Employee



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
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse_lazy)
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
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse_lazy)
        return redirect('/subject/')

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
