from django.db import models
import os, time, uuid
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User
from django.urls import reverse

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # eg: filename = 'my uploaded file.jpg'
        ext = filename.split('.')[-1]  #eg: 'jpg'
        uid = uuid.uuid4().hex[:10]    #eg: '567ae32f97'

        # eg: 'my-uploaded-file'
        new_name = '-'.join(filename.replace('.%s' % ext, '').split())

        # eg: 'my-uploaded-file_64c942aa64.jpg'
        renamed_filename = '%(new_name)s_%(uid)s.%(ext)s' % {'new_name': new_name, 'uid': uid, 'ext': ext}

        # eg: 'images/2017/01/29/my-uploaded-file_64c942aa64.jpg'
        return os.path.join(self.path, renamed_filename)
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
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=30)
    department_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    course_aliases=models.CharField(max_length=30)
    duration=models.CharField(max_length=1,choices=d,default=2)
    no_of_semestars=models.CharField(max_length=1,choices=d,default=4)
    approved_university=models.CharField(max_length=30)
    image_path = time.strftime('syllabus/%Y/%m/%d')    
    syllabus=models.ImageField(upload_to=PathAndRename(image_path))    
    remarks=models.TextField()

    def __str__(self):
        return self.course_name
    def get_absolute_url(self):
        return reverse('course_edit',kwargs={'pk':self.pk})

    

