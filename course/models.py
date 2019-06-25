from django.db import models
#from student.models import StudentEnquiry


class Department(models.Model):
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.department
class Course(models.Model):
    d=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
    )
    course_name=models.CharField(max_length=30)
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    course_aliases=models.CharField(max_length=30)
    duration=models.IntegerField(choices=d,default=2)
    no_of_semestars=models.CharField(max_length=1,choices=d,default=4)
    approved_university=models.CharField(max_length=30)
    #syllabus=models.FileField(upload_to='course/syllabus/',blank=True)
    remarks=models.TextField()

    def __str__(self):
        return self.course_name



