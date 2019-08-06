from django.db import models
from coursemanagement.models import Stream, Course, Batch
from academics.models import Semestar, Subject
from student.models import Student
from employee.models import Employee

class LessonPlan(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_number = models.IntegerField()
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    topic = models.CharField(max_length=250, verbose_name="Title")
    remark = models.TextField(null=True, blank=True)
    actual_duration = models.CharField(max_length=20, null=True, blank=True)
    actual_remark = models.TextField(null=True, blank=True)
    class_date = models.DateField(null=True, blank=True)
    attendance_count = models.IntegerField(default=0)


class Attendance(models.Model):
    Attendance_Choice = (
        ('A','A'),
        ('P','P'),
        ('L','L'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, on_delete=models.CASCADE,null=True, blank=True)
    attendance_type = models.CharField(max_length=3, choices=Attendance_Choice, default='P')
    remark = models.TextField(null=True, blank=True)


