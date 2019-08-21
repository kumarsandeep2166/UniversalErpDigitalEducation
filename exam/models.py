from django.db import models

class ExamType(models.Model):
    exam_type = models.CharField(max_length=250)
    
