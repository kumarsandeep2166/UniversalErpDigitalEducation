from django.db import models
from student.models import Districts, State, Country
from django.core.validators import RegexValidator
from coursemanagement.models import Stream
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=15)    

    def __str__(self):
        return self.name

class Designation(models.Model):
    designation = models.CharField(max_length=50)
    
    def __str__(self):
        return self.designation


class Employee(models.Model):
    BLOOD_GROUP=(('A+ve','A+ve'),('A-ve','A-ve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'),('O+ve','O+ve'),('O-ve','O-ve'))
    
    ttl=(
        ('mr','Mr.'),
        ('ms','Mrs.'),
        ('miss','Miss'),
        ('dr','Dr.'),
    )
    national=(
        ('in','Indian'),
    )
    caste=(
        ('Gen','GEN'),
        ('sc','SC'),
        ('st','ST'),
        ('obc','OBC'),
        ('others','Others'),
    )
    scale=(
        ('5th','5th Pay'),
        ('6th','6th Pay'),
        ('cons','Consolidated'),
    )
    type_join=(
        ('part','Part Time'),
        ('full','Full Time'),
        ('part','Contracted'),
    )
    GENDER_CHOICES=(        
            ('M', 'Male'),
            ('F', 'Female'),
            ('O','others')
    )
    RELIGION_CHOICES=(
        ('H','Hindu'),
        ('M','Muslim'),
        ('C','Christian'),
        ('O','Others'),
    )
    u_degree=(
        ('b.tech','B.Tech'),
        ('bachlr','Bachelors'),
        ('be','BE'),
    )
    m_degree=(
        ('m.tech','M.Tech'),
        ('master','Masters'),
        ('me','ME'),
    )
    physically_handicap=(
        ('y','Yes'),
        ('n','No'),
    )
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank= True)
    title=models.CharField(max_length=5,choices=ttl,default='Mr.')
    first_name=models.CharField(max_length=15)
    middle_name=models.CharField(max_length=15,null=True,blank= True)
    last_name=models.CharField(max_length=15)
    date_of_birth=models.DateTimeField(auto_now_add=False)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,default='Male')
    fathers_name=models.CharField(max_length=40)
    mothers_name=models.CharField(max_length=40,blank=False)
    phone_no=models.CharField(max_length=10,blank=False,validators=[RegexValidator('^[0-9]{10}$', message="Phone Number must be of 12 Digits")])
    aadhar_no=models.CharField(max_length=12,validators=[RegexValidator('^[0-9]{12}$', message="Aadhar Number must be of 12 Digits")])
    pan_no=models.CharField(max_length=15,blank=False)
    epfo_no=models.CharField(max_length=25,blank=False)
    email=models.EmailField()    
    nationality=models.CharField(max_length=10,choices=national,blank=False)
    caste=models.CharField(max_length=5,choices=caste,default='Others',blank=False)
    religion=models.CharField(max_length=20,choices=RELIGION_CHOICES,default='Hindu')
    scale_of_pay=models.CharField(max_length=15,choices=scale,default=20)
    type_of_joining=models.CharField(max_length=15,choices=type_join,default='Full Time')
    communication_address=models.TextField()
    communication_lane_address=models.CharField(max_length=70)
    landmark=models.CharField(max_length=70)
    pin=models.CharField(max_length=6,validators=[RegexValidator('^[0-9]{6}$', message="")])
    city=models.CharField(max_length=30)
    district=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    country=models.CharField(max_length=25)
    bank_name=models.CharField(max_length=25,blank=True)
    bank_account_number=models.IntegerField()
    bank_ifsc_code=models.CharField(max_length=25,blank=True)
    bank_branch=models.CharField(max_length=25,blank=True)
    tenth_subjects=models.CharField(max_length=20,blank=False)
    tenth_school=models.CharField(max_length=20,blank=False)
    tenth_board=models.CharField(max_length=20,blank=False)    
    tenth_full_mark=models.IntegerField(blank=False)
    tenth_secured_mark=models.IntegerField(blank=False)
    tenth_percentage=models.FloatField(blank=False)
    twelth_stream=models.CharField(max_length=20,blank=False)
    twelth_college=models.CharField(max_length=20,blank=False)
    twelth_board=models.CharField(max_length=20,blank=False)       
    #twelth_university=models.CharField(max_length=20,blank=True)
    twelth_full_mark=models.IntegerField(blank=False)
    twelth_secured_mark=models.IntegerField(blank=False)
    tewlth_percentage=models.FloatField(blank=False)    
    degree_stream=models.CharField(max_length=20,blank=False)
    degree_college=models.CharField(max_length=20,blank=False)
    degree_university=models.CharField(max_length=20,blank=False)
    degree_full_mark=models.IntegerField(blank=True,null=True)
    degree_secured_mark=models.IntegerField(blank=True,null=True)
    degree_percentage=models.FloatField(blank=False)
    postdegree_stream=models.CharField(max_length=20,blank=True)
    postdegree_college=models.CharField(max_length=20,blank=True)
    postdegree_university=models.CharField(max_length=20,blank=True)
    postdegree_full_mark=models.IntegerField(blank=True,null=True)
    postdegree_secured_mark=models.IntegerField(blank=True,null=True)
    postdegree_percentage=models.FloatField(null=True,blank=True)
    teaching_experience=models.IntegerField(blank=False)
    industry_experience=models.IntegerField(blank=False)
    experience_details=models.TextField(blank=True)
    last_appointment_type=models.CharField(max_length=20,choices=type_join,default='Full Time')
    last_payment_scale=models.CharField(max_length=20,choices=scale,default='5th pay')
    other_qualifiaction=models.CharField(max_length=15,blank=True)
    area_of_specialization=models.CharField(max_length=50)
    ug_degree=models.CharField(max_length=30,choices=u_degree,default='B.Tech',blank=False)
    pg_degree=models.CharField(max_length=25,choices=m_degree,default='M.Tech',blank=False)    
    patents_issued=models.IntegerField(null=True,blank=True)
    no_of_pg_projects=models.IntegerField(blank=True)
    physically_handicaped=models.CharField(choices=physically_handicap,max_length=1,blank=False)
    national_journal_no=models.IntegerField(null=True,blank=True)    
    international_journal_no=models.IntegerField(null=True,blank=True)
    journal_details=models.TextField(blank=True)
    national_conference_no=models.IntegerField(null=True,blank=True)    
    international_conference_no=models.IntegerField(null=True,blank=True)
    conference_details=models.TextField(null=True,blank=True)
    status=models.BooleanField(default=True)
    
    employee_category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=False)
    employee_designation=models.ForeignKey(Designation,on_delete=models.SET_NULL,null=True,blank=False)
    employee_department=models.ForeignKey(Stream,on_delete=models.SET_NULL,null=True,blank=False)

    def __str__(self):
        return '{}-{}-{}'.format(self.first_name,self.middle_name,self.last_name)
    # def get_absolute_url(self):
    #     return reverse('employee_detail', kwargs={
    #         'pk': self.pk
    #     })

