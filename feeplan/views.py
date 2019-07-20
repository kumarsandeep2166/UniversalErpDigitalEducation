from django.shortcuts import render,redirect
from .models import FeesPlanType,ApproveFeeplanType
#from django.forms import modelformset_factory,inlineformset_factory
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .forms import FeesPlanTypeForm,ApproveFeePlanTypeForm
from coursemanagement.models import Stream, Course, Batch
from django.db.models import Q
from student.models import Enrollment

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

class ApproveFeePlanCreate(CreateView):
    model=ApproveFeeplanType
    template_name='feeplan/feecollection.html'
    form_class=ApproveFeePlanTypeForm

    def get(self, request, *args, **kwargs):
        context={'form':ApproveFeePlanTypeForm()}
        return render(request, 'feeplan/feecollection.html', context)

    def post(self, request, *args, **kwargs):
        form=ApproveFeePlanTypeForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                form.save()
                return redirect("feeplan_list")
        return render(request, 'feeplan/feecollection.html', {'form':form})