from django.contrib import admin
from .models import Semestar, Subject, SubjectTeacher, LessonPlan,Attendance

# Register your models here.

admin.site.register(Semestar)
admin.site.register(Subject)
admin.site.register(Attendance)
