from django import forms
from .models import Semestar, Subject, SubjectTeacher, LessonPlan
from coursemanagement.models import Stream, Course, Batch
from employee.models import Employee


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
        fields = ('__all__')

class SubjectTeacherForm(forms.ModelForm):
    stream = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Stream.objects.all()])
    course = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Course.objects.all()])
    batch = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Batch.objects.all()])
    semestar = forms.ChoiceField(choices=[(o.id, str(o)) for o in Semestar.objects.all()])
    class Meta:
        model = SubjectTeacher
        fields = ('__all__')