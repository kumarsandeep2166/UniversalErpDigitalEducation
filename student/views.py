from django.shortcuts import render,redirect
#from django.views.generic.edit import FormView
from .models import (StudentDetail,ParentDetails,
                    Tenth,Twelth,Degree,PostDegree,
                    PresentAddress,PermanentAddress,Entrance,
                    AttachmentDetails)
from .forms import (StudentEnquiryForm,StudentDetailForm,
                    ParentDetailsForm,EntranceForm,TenthForm,TwelthForm,DegreeForm,PostDegreeForm,
                    PresentAddressForm,PermanentAddressForm,AttachmentForm)
from django.views.generic import ListView,DetailView,DeleteView
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
   
def studentregister(request):
    form_a=StudentDetailForm()
    form_b=ParentDetailsForm()
    form_c=TenthForm()
    form_d=TwelthForm()
    form_e=DegreeForm()
    form_f=PostDegreeForm()
    form_g=PresentAddressForm()
    form_h=EntranceForm()
    form_i=AttachmentForm()
    form_j=PermanentAddressForm()
    if request.method=="POST":
        form_a=StudentDetailForm(request.POST or None)
        form_b=ParentDetailsForm(request.POST or None)
        form_c=TenthForm(request.POST or None)
        form_d=TwelthForm(request.POST or None)
        form_e=DegreeForm(request.POST or None)
        form_f=PostDegreeForm(request.POST or None)
        form_g=PresentAddressForm(request.POST or None)
        form_h=EntranceForm(request.POST or None)
        form_i=AttachmentForm(request.POST or None,request.FILES or None)
        form_j=PermanentAddressForm(request.POST or None)
        if form_a.is_valid() and form_b.is_valid() and form_c.is_valid() and form_d.is_valid() and form_e.is_valid() and form_f.is_valid() and form_g.is_valid() and form_h.is_valid() and form_i.is_valid() and form_j.is_valid():
            form_a.save()
            form_b.save()
            form_c.save()
            form_d.save()
            form_e.save()
            form_f.save()
            form_g.save()
            form_h.save()
            form_i.save()
            form_j.save()
        context={
            'form1':form_a,
            'form2':form_b,
            'form3':form_c,
            'form4':form_d,
            'form5':form_e,
            'form6':form_f,
            'form7':form_g,
            'form8':form_h,
            'form9':form_i,
            'form10':form_j,
        }
        return render(request,'student/studentadmissionform.html',context)
    else:
        form_a=StudentDetailForm()
        form_b=ParentDetailsForm()
        form_c=TenthForm()
        form_d=TwelthForm()
        form_e=DegreeForm()
        form_f=PostDegreeForm()
        form_g=PresentAddressForm()
        form_h=EntranceForm()
        form_i=AttachmentForm()
        form_j=PermanentAddressForm()
        context={
            'form1':form_a,
            'form2':form_b,
            'form3':form_c,
            'form4':form_d,
            'form5':form_e,
            'form6':form_f,
            'form7':form_g,
            'form8':form_h,
            'form9':form_i,
            'form10':form_j,
        }
        return render(request,'student/studentadmissionform.html',context)


class StudentListView(ListView):
    context_object_name='student_list'
    template_name='student/student_list.html'
    queryset=StudentDetail.objects.all()

    def get_context_data(self,**kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['parents']=ParentDetails.objects.all()
        context['tenth']=Tenth.objects.all()
        context['tewlth']=Twelth.objects.all()
        context['degree']=Degree.objects.all()
        context['post_degree']=PostDegree.objects.all()
        context['entrance']=Entrance.objects.all()
        context['pres_address']=PresentAddress.objects.all()
        context['attach']=AttachmentDetails.objects.all()
        return context

    

class StudentDetailView(DetailView):
    pass
class StudentDeleteView(DeleteView):
    pass