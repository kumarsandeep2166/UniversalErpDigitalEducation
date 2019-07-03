from django.contrib import admin

# Register your models here.
from .models import Stream,Section,Batch,Course,FeesManagement

admin.site.register(Stream)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Section)
admin.site.register(FeesManagement)