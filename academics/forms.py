from django import forms
from .models import Semestar, Subject, SubjectTeacher, LessonPlan, Attendance
from coursemanagement.models import Stream, Course, Batch
from employee.models import Employee
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class SemestarForm(forms.ModelForm):
    class Meta:
        model = Semestar
        fields = ('__all__')

class SubjectForm(forms.ModelForm):
    stream = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Stream.objects.all()])
    course = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Course.objects.all()])
    batch = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Batch.objects.all()])
    class Meta:
        model = Subject
        fields = ('semestar','name',)
    
    
class SubjectTeacherForm(forms.ModelForm):
    stream = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Stream.objects.all()])
    course = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Course.objects.all()])
    batch = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Batch.objects.all()])
    semestar = forms.ChoiceField(choices=[(o.id, str(o)) for o in Semestar.objects.all()])
    class Meta:
        model = SubjectTeacher
        fields = ('__all__')

 

class LessonPlanForm(forms.ModelForm):
    stream = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Stream.objects.all()])
    course = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Course.objects.all()])
    batch = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Batch.objects.all()])
    semestar = forms.ChoiceField(choices=[(o.id, str(o)) for o in Semestar.objects.all()])
    subject = forms.ChoiceField(choices=[(o.id, str(o)) for o in Subject.objects.all()])
    class_number = forms.IntegerField(label='Cls No.')
    class Meta:
        model = LessonPlan
        fields = ('__all__')

class AttendanceForm(forms.ModelForm):
    stream = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Stream.objects.all()])
    course = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Course.objects.all()])
    batch = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Batch.objects.all()])
    semestar = forms.ChoiceField(choices=[(o.id, str(o)) for o in Semestar.objects.all()])
    subject = forms.ChoiceField(choices=[(o.id, str(o)) for o in Subject.objects.all()])
    
    class Meta:
        model = Attendance
        fields = ('__all__')


