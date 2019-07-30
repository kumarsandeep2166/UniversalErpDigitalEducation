from django.db import models
from coursemanagement.models import Course, Stream, Batch
from employee.models import Employee
from student.models import Student

SEMESTAR_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
    ('5th', '5th'),
    ('6th', '6th'),
    ('7th', '7th'),
    ('8th', '8th'),
)

class Semestar(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    name = models.CharField(max_length=10,choices=SEMESTAR_CHOICES,default='1st')

    def __str__(self):
        return self.name


class Subject(models.Model):
    semestar = models.ForeignKey(Semestar, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubjectTeacher(models.Model):
    teacher = models.ForeignKey(Employee, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class LessonPlan(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_number = models.IntegerField()
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    topic = models.CharField(max_length=250)
    remark = models.TextField(null=True, blank=True)
