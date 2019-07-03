from django import forms

from .models import Stream,Section,Batch,Course

class StreamForm(forms.ModelForm):
    class Meta:
        model=Stream
        fields=('__all__')

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=('__all__')

class BatchForm(forms.ModelForm):
    class Meta:
        model=Batch
        fields=('__all__')
class SectionForm(forms.ModelForm):
    class Meta:
        model=Section
        fields=('__all__')