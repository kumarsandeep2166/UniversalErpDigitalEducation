from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['course_name'].queryset=Course.objects.none()   
    
        if 'department' in self.data:
            try:
                department_id=int(self.data.get('department'))
                self.fields['course_name'].queryset=Course.objects.filter(department_id=department_id).order_by('course_name')
                
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['course_name'].queryset=self.instance.department.course_name_set.order_by('branch')
