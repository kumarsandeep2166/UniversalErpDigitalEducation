import os, time, uuid
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import datetime
from django.urls import reverse

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]
def current_year():
    return datetime.date.today().year
class Department(models.Model):
    department=models.CharField(max_length=50)
    def __str__(self):
        return self.department
class Branch(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    branch=models.CharField(max_length=50)
    def __str__(self):
        return self.branch

class Country(models.Model):
    country=models.CharField(max_length=30)
    def __str__(self):
        return self.country
class State(models.Model):
    state=models.CharField(max_length=30)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.state
class Districts(models.Model):
    district=models.CharField(max_length=30)
    state=models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.district

class StudentEnquiry(models.Model):
    SHIFT_CHOICES=(
        ('FIRST SHIFT','First Shift'),
        ('SECOND SHIFT','Second Shift')
    )
    YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    phone_no=models.CharField(max_length=10, validators=[RegexValidator('^[0-9]{10}$', message="Phone number must be of 10 digit!!")])
    email_id=models.EmailField()
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=False)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True,blank=False)
    shift=models.CharField(max_length=26, choices=SHIFT_CHOICES, default='First Shift')
    last_education=models.TextField()
    entrance=models.CharField(max_length=40)
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year())
    score=models.IntegerField()
    def __str__(self):
        return '{0}-{1}-{2}'.format(self.first_name,self.middle_name,self.last_name)
class StudentDetail(models.Model):
    BLOOD_GROUP=(('A+ve','A+ve'),('A-ve','A-ve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'),('O+ve','O+ve'),('O-ve','O-ve'))
    CASTE=(('Gen','GEN'),('SC','SC'),('ST','ST'),('OBC','OBC'),('Others','Others'))
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female')
        )

    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    blood_group=models.CharField(max_length=5,choices=BLOOD_GROUP,default='O+ve')
    caste=models.CharField(max_length=10,choices=CASTE,default='Others')
    sub_caste=models.CharField(max_length=10,choices=CASTE,default='Others')
    place_of_birth=models.CharField(max_length=20)
    aadhar_number=models.CharField(max_length=12,validators=[RegexValidator('^[0-9]{12}$', message="Aadhar Number must be of 12 Digits")])
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)

    def __str__(self):
        return '{}-{}-{}'.format(self.first_name,self.middle_name,self.last_name)
    
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={
            'pk': self.pk
        })
class ParentDetails(models.Model):
    OCCUPATION1=(
        ('GE','Govt. Employee'),
        ('PE','Private Employee'),
        ('SE','Self Employed'),
        ('B','Businessman'),
        ('O','Others'),        
    )
    OCCUPATION2=(
        ('GE','Govt. Employee'),
        ('PE','Private Employee'),
        ('SE','Self Employed'),
        ('B','Businesswoman'),
        ('HM','Home Maker'),
        ('O','Others'),        
    )
    fathers_name=models.CharField(max_length=20)
    fathers_occupation=models.CharField(max_length=30,choices=OCCUPATION1,default='Others')
    fathers_date_of_birth=models.DateField()
    fathers_phone_no=models.CharField(max_length=10, validators=[RegexValidator('^[0-9]{10}$', message="Please Enter a Valid Phone Number")])
    fathers_email_id=models.EmailField()
    fathers_annual_income=models.CharField(max_length=10)

    mothers_name=models.CharField(max_length=20)
    mothers_occupation=models.CharField(max_length=30,choices=OCCUPATION2,default='Others')
    mothers_date_of_birth=models.DateField(blank=True)
    mothers_phone_no=models.CharField(max_length=10, validators=[RegexValidator('^[0-9]{10}$', message="Please Enter a Valid Phone Number")])
    mothers_email_id=models.EmailField(blank=True)
    mothers_annual_income=models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.fathers_name
class Tenth(models.Model):
    board=models.CharField(max_length=20,blank=False)
    stream=models.CharField(max_length=20,blank=False)
    school=models.CharField(max_length=20,blank=False)
    university=models.CharField(max_length=20,blank=False)
    full_mark=models.IntegerField()
    secured_mark=models.IntegerField()
    
    @property
    def percentage_mark(self):
        percentage=self.secured_mark/self.full_mark*100
        return percentage
    percentage=models.FloatField('percentage',max_length=4)   
    

    def __str__(self):
        return self.board
class Twelth(models.Model):
    board=models.CharField(max_length=20,blank=False)
    stream=models.CharField(max_length=20,blank=False)
    school=models.CharField(max_length=20,blank=False)
    university=models.CharField(max_length=20,blank=False)
    full_mark=models.IntegerField()
    secured_mark=models.IntegerField()

    @property
    def percentage_mark(self):
        percentage=self.secured_mark/self.full_mark*100
        return percentage
    percentage=models.FloatField('percentage',max_length=4)
    def __str__(self):
        return self.board  
class Degree(models.Model):
    board=models.CharField(max_length=20,blank=False)
    stream=models.CharField(max_length=20,blank=False)
    school=models.CharField(max_length=20,blank=False)
    university=models.CharField(max_length=20,blank=False)
    full_mark=models.IntegerField()
    secured_mark=models.IntegerField()
    
    @property
    def percentage_mark(self):
        percentage=self.secured_mark/self.full_mark*100
        return percentage
    percentage=models.FloatField('percentage',max_length=4)   
    

    def __str__(self):
        return self.board  
class PostDegree(models.Model):
    board=models.CharField(max_length=20,blank=False)
    stream=models.CharField(max_length=20,blank=False)
    school=models.CharField(max_length=20,blank=False)
    university=models.CharField(max_length=20,blank=False)
    full_mark=models.IntegerField()
    secured_mark=models.IntegerField()

    @property
    def percentage_mark(self):
        percentage=self.secured_mark/self.full_mark*100
        return percentage
    percentage=models.FloatField('percentage',max_length=4)      

    def __str__(self):
        return self.board  

class PresentAddress(models.Model):
    house_plot_no=models.TextField()
    Lane=models.TextField()
    pin=models.IntegerField(blank=False,validators=[RegexValidator('^[0-9]{6}$', message="")])
    district=models.ForeignKey(Districts,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    same_address=models.BooleanField(default=False)

    def __str__(self):
        return '{0}-{1}'.format(self.district,self.pin)

class PermanentAddress(models.Model):
    house_plot_no=models.TextField()
    Lane=models.TextField()
    pin=models.IntegerField(blank=False,validators=[RegexValidator('^[0-9]{6}$', message="")])
    district=models.ForeignKey(Districts,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return '{0}-{1}'.format(self.district,self.pin)

class Entrance(models.Model):
    YEAR_CHOICES = [(r,r) for r in range(2000, datetime.date.today().year+1)]
    name=models.CharField(max_length=20)
    year=models.IntegerField(('year'), choices=year_choices(), default=current_year())
    score=models.IntegerField()

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.name,self.year,self.score)

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
class AttachmentDetails(models.Model):    
    image_path = time.strftime('attachments/%Y/%m/%d')
    #image = models.ImageField(upload_to=PathAndRename(image_path))
    student_image=models.ImageField(upload_to=PathAndRename(image_path))
    tenth=models.ImageField(upload_to=PathAndRename(image_path))
    twelth=models.ImageField(upload_to=PathAndRename(image_path))
    degree=models.ImageField(upload_to=PathAndRename(image_path))
    clc=models.ImageField(upload_to=PathAndRename(image_path))
    conduct_certificate=models.ImageField(upload_to=PathAndRename(image_path))
    migration=models.ImageField(upload_to=PathAndRename(image_path))
    birth_certificate=models.ImageField(upload_to=PathAndRename(image_path))
    address=models.ImageField(upload_to=PathAndRename(image_path))
    thumb=models.ImageField(upload_to=PathAndRename(image_path))
    signature=models.ImageField(upload_to=PathAndRename(image_path))
    def __str__(self):
        return "Images uploaded for:{}".format(self.student_image.name)


class StudentApplicationForm(models.Model):
    enrollment_date=models.DateTimeField(auto_now_add=True)
    admission_no=models.CharField(max_length=10, validators=[RegexValidator('^[0-9]{10}$', message="Please Enter Correct Data")])
    admission_date=models.DateTimeField(auto_now_add=True)
    course=models.ForeignKey(Branch,on_delete=models.CASCADE)
    student_detail=models.ForeignKey(StudentDetail,on_delete=models.CASCADE)
    parent_details=models.ForeignKey(ParentDetails,on_delete=models.CASCADE)
    tenth=models.ForeignKey(Tenth,on_delete=models.SET_NULL,null=True)
    twelth=models.ForeignKey(Twelth,on_delete=models.SET_NULL,null=True)
    degree=models.ForeignKey(Degree,on_delete=models.SET_NULL,null=True)
    post_degree=models.ForeignKey(PostDegree,on_delete=models.SET_NULL,null=True)
    entrances=models.ForeignKey(Entrance,on_delete=models.CASCADE)
    present_address=models.ForeignKey(PresentAddress,on_delete=models.CASCADE)
    permanent_address=models.ForeignKey(PermanentAddress,on_delete=models.CASCADE) 
    images=models.ForeignKey(AttachmentDetails,on_delete=models.CASCADE)   

    def __str__(self):
        return self.admission_no







