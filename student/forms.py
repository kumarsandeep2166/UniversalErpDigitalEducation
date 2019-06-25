from django import forms
from .models import (StudentEnquiry, Branch,StudentApplicationForm,
                    StudentDetail,ParentDetails,Tenth,
                    Twelth,Degree,PostDegree,
                    Entrance,PresentAddress,PermanentAddress,AttachmentDetails)
from datetime import datetime
#from django.views.generic.edit import FormView
class StudentEnquiryForm(forms.ModelForm):
    
    class Meta:
        model=StudentEnquiry
        fields=('first_name','middle_name','last_name','date_of_birth','phone_no','email_id','department','branch','shift','last_education','entrance','year','score')
        SHIFT_CHOICES=(("First Shift","First Shift"),("Second Shift","Second Shift")
        )
        
        widgets={
            'shift':forms.Select(choices=SHIFT_CHOICES,attrs={'class': 'form-control'}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['branch'].queryset=Branch.objects.none()   
    
        if 'department' in self.data:
            try:
                department_id=int(self.data.get('department'))
                self.fields['branch'].queryset=Branch.objects.filter(department_id=department_id).order_by('branch')
                
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset=self.instance.department.branch_set.order_by('branch')


class StudentDetailForm(forms.ModelForm):
    class Meta:
        model=StudentDetail
        fields='__all__'
        template_name='student/studentadmissionform.html'

class ParentDetailsForm(forms.ModelForm):
    class Meta:
        model=ParentDetails
        fields='__all__'
        template_name='student/studentadmissionform.html'

class TenthForm(forms.ModelForm):
    class Meta:
        model=Tenth
        fields='__all__'
        template_name='student/studentadmissionform.html'

class TwelthForm(forms.ModelForm):
    class Meta:
        model=Twelth
        fields='__all__'
        template_name='student/studentadmissionform.html'

class DegreeForm(forms.ModelForm):
    class Meta:
        model=Degree
        fields='__all__'
        template_name='student/studentadmissionform.html'

class PostDegreeForm(forms.ModelForm):
    class Meta:
        model=PostDegree
        fields='__all__'
        template_name='student/studentadmissionform.html'

class EntranceForm(forms.ModelForm):
    class Meta:
        model=Entrance
        fields='__all__'
        template_name='student/studentadmissionform.html'

class PresentAddressForm(forms.ModelForm):
    class Meta:
        model=PresentAddress
        fields='__all__'
        template_name='student/studentadmissionform.html'
class PermanentAddressForm(forms.ModelForm):
    class Meta:
        model=PermanentAddress
        fields='__all__'
        template_name='student/studentadmissionform.html'
class AttachmentForm(forms.ModelForm):
    class Meta:
        model=AttachmentDetails
        fields='__all__'
        template_name='student/studentadmissionform.html'