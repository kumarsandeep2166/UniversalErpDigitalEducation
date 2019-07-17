from django.db import models
from coursemanagement.models import FeesManagementSetting,Feestype,Course,Stream,Batch,Section
from student.models import Student,Enrollment



class FeesPlanType(models.Model):    
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    fees_type=models.CharField(max_length=10)
    actual_fees=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.fees_type


class ApproveFeeplanType(models.Model):
    enrollment_num=models.ForeignKey(Enrollment,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    fees_node=models.ForeignKey(FeesPlanType,on_delete=models.CASCADE)
    approve_fees=models.DecimalField(max_digits=10,decimal_places=2)
    # no_of_installments=models.IntegerField()
    # due_date=models.DateField()
    
    def __str__(self):
        return '{}/{}/{}/{}'.format(self.course,self.batch,self.enrollment_num,self.fees_node)