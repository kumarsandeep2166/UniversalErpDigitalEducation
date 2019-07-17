from django import forms
from .models import (StudentEnquiry, Branch,Student,Employee,Enrollment)
from datetime import datetime


#from django.views.generic.edit import FormView
class StudentEnquiryForm(forms.ModelForm):
    
    class Meta:
        model=StudentEnquiry
        fields=('first_name','middle_name','last_name','date_of_birth','phone_no','email_id','department','branch','shift','last_education','entrance','year','score')
        ordering_by=['-id']
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

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1990,2030)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])
    fathers_date_of_birth=forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1950,2010)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])
    mothers_date_of_birth=forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1950,2010)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])
    #date_of_admission=forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(2000,2020)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])
    tenth_board=forms.CharField(label='')
    tenth_subjects=forms.CharField(label='')
    tenth_school=forms.CharField(label='')
    tenth_full_mark=forms.IntegerField(label='')
    tenth_secured_mark=forms.IntegerField(label='')
    tenth_percentage=forms.FloatField(label='')


    twelth_board=forms.CharField(label='')
    twelth_stream=forms.CharField(label='')
    twelth_school=forms.CharField(label='')
    twelth_full_mark=forms.IntegerField(label='')
    twelth_secured_mark=forms.IntegerField(label='')
    tewlth_percentage=forms.FloatField(label='')
    
    degree_stream=forms.CharField(label='')
    degree_college=forms.CharField(label='')
    degree_university=forms.CharField(label='')
    degree_full_mark=forms.IntegerField(label='')
    degree_secured_mark=forms.IntegerField(label='')
    degree_percentage=forms.FloatField(label='')


    postdegree_stream=forms.CharField(label='')
    postdegree_college=forms.CharField(label='')
    postdegree_university=forms.CharField(label='')
    postdegree_full_mark=forms.IntegerField(label='')
    postdegree_secured_mark=forms.IntegerField(label='')
    postdegree_percentage=forms.FloatField(label='')
    present_same_address=forms.BooleanField(label='',required=False)
    entrance_name=forms.CharField(label='')
    entrance_year=forms.Select()
    entrance_score=forms.CharField(label='')
    student_pic=forms.ImageField(label='')
    student_tenth=forms.ImageField(label='')
    tenth_marksheet=forms.ImageField(label='')
    student_twelth=forms.ImageField(label='')
    tewlth_marksheet=forms.ImageField(label='')
    student_degree=forms.ImageField(label='')
    degree_marksheet=forms.ImageField(label='')
    student_clc=forms.ImageField(label='')
    student_conduct_certificate=forms.ImageField(label='')
    student_migration=forms.ImageField(label='')
    student_birth_certificate=forms.ImageField(label='')
    student_address=forms.ImageField(label='')
    student_thumb=forms.ImageField(label='')
    student_signature=forms.ImageField(label='')
    term_and_condition=forms.BooleanField(label='',required=False)
    class Meta:
        model=Student
        fields='__all__'
        template_name='student/studentadmissionform.html'
        # widgets={
        #     'student_pic':forms.FileField(attrs={'onchange': "readURL(this);"})
        # }
class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1990,2030)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])
    tenth_subjects = forms.CharField(label='')
    tenth_school = forms.CharField(label='')
    tenth_board=forms.CharField(label='')
    tenth_full_mark=forms.IntegerField(label='')
    tenth_secured_mark=forms.IntegerField(label='')
    tenth_percentage=forms.FloatField(label='')
    
    twelth_board=forms.CharField(label='')
    twelth_stream=forms.CharField(label='')
    twelth_college=forms.CharField(label='')
    twelth_full_mark=forms.IntegerField(label='')
    twelth_secured_mark=forms.IntegerField(label='')
    tewlth_percentage=forms.FloatField(label='')
    
    degree_stream=forms.CharField(label='')
    degree_college=forms.CharField(label='')
    degree_university=forms.CharField(label='')
    degree_full_mark=forms.IntegerField(label='')
    degree_secured_mark=forms.IntegerField(label='')
    degree_percentage=forms.FloatField(label='')


    postdegree_stream=forms.CharField(label='')
    postdegree_college=forms.CharField(label='')
    postdegree_university=forms.CharField(label='')
    postdegree_full_mark=forms.IntegerField(label='')
    postdegree_secured_mark=forms.IntegerField(label='')
    postdegree_percentage=forms.FloatField(label='')
    class Meta:
        model=Employee
        fields=('__all__')
        template_name='student/employeemanagement.html'
    
class EnrollmentForm(forms.ModelForm):
    student_name=forms.CharField(max_length=50)
    date_of_admission = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1920,2010)]),input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d/%m/%y'])
    class Meta:
        model=Enrollment
        fields=('course','stream','batch','enrollment_number','date_of_admission')
        