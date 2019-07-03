from django.db import models
from django.core.validators import MaxValueValidator

class FeesManagement(models.Model):
    fee_type=models.CharField(max_length=20)
    actual_amount=models.IntegerField(validators=[MaxValueValidator(9999999)],blank=True)
    discount_amount=models.IntegerField(validators=[MaxValueValidator(9999999)],blank=True)


    def __str__(self):
        return self.fee_type


class Stream(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Course(models.Model):
    Exam_choices=(
        ('sem','SEMESTER'),
        ('yr','YEARLY'),
        ('tr','TRIMESTER')
    )
    duration_choice=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    )
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)
    course_code=models.CharField(max_length=15)
    course_name=models.CharField(max_length=50)
    course_aliases=models.CharField(max_length=30)
    duration=models.CharField(max_length=1,choices=duration_choice,default='4')
    approved_date=models.DateTimeField(auto_now_add=False)
    exam_pattern=models.CharField(max_length=3,choices=Exam_choices,default='SEMESTER')
    affiliated_body=models.CharField(max_length=30)
    syllabus=models.FileField(blank=False)
    remark=models.TextField()
    #fees=models.ManyToManyField(FeesManagement)

    def __str__(self):
        return self.course_name
class Batch(models.Model):
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_no=models.CharField(max_length=50)
    starting_date=models.DateTimeField(auto_now_add=False)
    ending_date=models.DateTimeField(auto_now_add=False)
    remark=models.TextField()

    def __str__(self):
        return self.batch_no
class Section(models.Model):
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_no=models.ForeignKey(Batch,on_delete=models.CASCADE)
    section_name=models.CharField(max_length=20)
    remark=models.TextField()

    def __str__(self):
        return self.section_name
