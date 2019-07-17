from django.shortcuts import render,redirect
from .models import Section,Stream,Batch,Course,Feestype,FeesManagementSetting
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from .forms import SectionForm,StreamForm,BatchForm,CourseForm,FeesForm,FeesManagementSettingForm
from django.urls import reverse_lazy
import string

class StreamCreateView(CreateView):
    model=Stream
    form_class=StreamForm
    template_name='coursemanagement/stream_form.html'
    def get_context_data(self,**kwargs):
        context=super(StreamCreateView,self).get_context_data(**kwargs)
        return context

    def get(self,request,*args,**kwargs):
        context={'form':StreamForm()}
        return render(request,'coursemanagement/stream_form.html',context)
    def post(self,request,*args,**kwargs):
        form=StreamForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('stream_list')
        return render(request,'coursemanagement/stream_form.html',{'form':form})

class StreamListView(ListView):
    template_name='coursemanagement/stream_list.html'    
    queryset=Stream.objects.all()
    context_object_name='stream_list'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class CourseCreateView(CreateView):
    model=Course
    form_class=CourseForm
    template_name='coursemanagement/course_create.html'

    def get_context_data(self,**kwargs):
        context=super(CourseCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        context={'form':CourseForm()}
        return render(request,'coursemanagement/course_form.html',context)
    def post(self,request,*args,**kwargs):
        form=CourseForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()     
            return redirect('course_list')   
        return render(request,'coursemanagement/course_form.html',{'form':form})

class BatchCreateView(CreateView):
    model=Batch
    form_class=BatchForm
    template_name='coursemanagement/batch_form.html'
    
    def get_context_data(self,**kwargs):
        context=super(BatchCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        context={'form':BatchForm()}
        return render(request,'coursemanagement/batch_form.html',context)
    def post(self,request,*args,**kwargs):
        form=BatchForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()  
            return redirect('batch_list')      
        return render(request,'coursemanagement/batch_form.html',{'form':form})


class SectionCreateView(CreateView):
    model=Section
    form_class=SectionForm
    template_name='coursemanagement/section_form.html'

    def get_context_data(self,**kwargs):
        context=super(SectionCreateView,self).get_context_data(**kwargs)
        return context
    def get(self,request,*args,**kwargs):
        context={'form':SectionForm()}
        return render(request,'coursemanagement/section_form.html',context)
        
    def post(self,request,*args,**kwargs):
        form=SectionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('section_list')
        return render(request,'coursemanagement/section_form.html',{'form':form})
class CourseUpdateView(UpdateView):
    model=Course
    fields='__all__'
    template_name='coursemanagement/course_edit.html'
    success_url=reverse_lazy('course_list')
class CourseListView(ListView):
    template_name='coursemanagement/course_list.html'
    context_object_name='courses'
    queryset=Course.objects.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
class CourseDetailView(DetailView):
    context_object_name='course_list'
    template_name='coursemanagement/course_detail.html'
    queryset=Course.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)       
        return context
class CourseDeleteView(DeleteView):
    model=Course
    success_url=reverse_lazy('course_list')

class BatchListView(ListView):
    template_name='coursemanagement/batch_list.html'
    context_object_name='batch'
    queryset=Batch.objects.all()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
class BatchDetailView(DetailView):
    context_object_name='batch_list'
    template_name='coursemanagement/batch_detail.html'
    queryset=Batch.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(BatchDetailView, self).get_context_data(**kwargs)       
        return context 

class BatchUpdateView(UpdateView):
    model=Batch
    fields='__all__'
    template_name='coursemanagement/batch_edit.html'
    success_url=reverse_lazy('batch_list')

class BatchDeleteView(DeleteView):
    model=Batch
    success_url=reverse_lazy('batch_list')


class SectionListView(ListView):
    template_name='coursemanagement/section_list.html'
    context_object_name='section_list'
    queryset=Section.objects.all()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class SectionDetailView(DetailView):
    context_object_name='section_list'
    template_name='coursemanagement/section_detail.html'
    queryset=Batch.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(SectionDetailView, self).get_context_data(**kwargs)       
        return context 

class SectionUpdateView(UpdateView):
    model=Section
    fields=('__all__')
    template_name='coursemanagement/section_edit.html'
    success_url=reverse_lazy('section_list')

class SectionDeleteView(DeleteView):
    model=Section
    success_url=reverse_lazy('section_list')

def load_course(request):
    stream_id=request.GET.get('stream')
    course=Course.objects.filter(stream_id=stream_id).order_by('-id')
    context={'course':course}
    return render(request,'coursemanagement/includes/course_ajax.html',context)

def load_batch(request):
    stream_id=request.GET.get('course')
    course=Course.objects.get(pk=stream_id)
    batch=Batch.objects.filter(course_name=course).order_by('-id')
    context={'batch':batch}
    return render(request,'coursemanagement/includes/batch_ajax.html',context)


def load_section(request):
    stream_id=request.GET.get('stream')
    course_id=request.GET.get('course_name')
    batch_id=request.GET.get('batch_no')
    section=Section.objects.filter(course_id=course_id,stream_id=stream_id,batch_id=batch_id).order_by('-id')
    context={'section':section}
    return render(request,'coursemanagement/includes/section_ajax.html',context)

def feesmanagement(request):
    form=FeesForm()
    if request.method=="POST":
        form=FeesForm(request.POST or None)
        #fee_type=request.cleaned_data.get('fee_type')
        if form.is_valid() :
            
            form.save()
            return redirect('fees_list')
    
    return render(request,'coursemanagement/feessetting.html',{'form':form})
class FeesTypeView(ListView):
    template_name='coursemanagement/fees_list.html'
    context_object_name='fees_list'
    queryset=Feestype.objects.all()
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context
    def get_queryset(self,*args):
        return Feestype.objects.all()
    
class FeesTypeEditView(UpdateView):
    model=Feestype
    fields=('__all__')
    template_name='coursemanagement/fees_edit.html'
    success_url=reverse_lazy('fees_list')
class FeesTypeDeleteView(DeleteView):
    model=Feestype
    template_name='coursemanagement/feestype_delete.html'
    success_url=reverse_lazy('fees_list')

def FeesManagementView(request):
    form=FeesManagementSettingForm()
    if request.method=="POST":
        form=FeesManagementSettingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('feesmanagement_list')
    return render(request,'coursemanagement/feesmanagment_create.html',{'form':form})
    
class FeesManagementSettingUpdateView(UpdateView):
    model=FeesManagementSetting
    fields=('__all__')
    template_name='coursemanagement/feesmanagement_edit.html'
    success_url=reverse_lazy('feesmanagement_list')

class FeesManagementSettingListView(ListView):
    template_name='coursemanagement/feesmanagement_list.html'
    context_object_name='feesmanagement_list'
    queryset=FeesManagementSetting.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

class FeesManagementSettingDetailView(DetailView):
    context_object_name='feesmanagement_detail'
    template_name='coursemanagement/feesmanagement_detail.html'
    queryset=FeesManagementSetting.objects.all()
    
    def get_context_data(self,**kwargs):
        context = super(FeesManagementSettingDetailView, self).get_context_data(**kwargs)       
        return context 

class FeesManagementSettingDeleteView(DeleteView):
    model=FeesManagementSetting
    template_name='coursemanagement/feesmanagement_delete.html'
    success_url=reverse_lazy('feesmanagement_list')