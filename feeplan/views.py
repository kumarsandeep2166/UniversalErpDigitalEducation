from django.shortcuts import render
from .models import FeesPlanType,ApproveFeeplanType
from django.forms import modelformset_factory,inlineformset_factory

def index(request):
    ExampleFormSet=modelformset_factory(FeesPlanType,fields=('stream','course','batch','fees_type','actual_fees',),extra=1)    
    if request.method=="POST":        
        form=ExampleFormSet(request.POST or None,request.FILES or None) 
        if form.is_valid():       
            instances=form.save(commit=False)
            for instance in instances:
                instance.save()
    else:
        form=ExampleFormSet() 
    return render(request,'feeplan/index.html',{'form':form})

def homefee(request,fee_id):
    fees_id=FeesPlanType.objects.get(pk=fee_id)
    return render(request,'feeplan/index.html',{})