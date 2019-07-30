from django import forms
from .models import Semestar, Subject, SubjectTeacher, LessonPlan
from coursemanagement.models import Stream, Course, Batch


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