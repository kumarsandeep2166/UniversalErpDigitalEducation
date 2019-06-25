from django.contrib import admin

from .models import (StudentEnquiry,
                        Branch,Department,
                        Districts,Country,State,
                        ParentDetails,
                        StudentDetail,
                        StudentApplicationForm,
                        Tenth,
                        Twelth,
                        Degree,Entrance,PermanentAddress,PresentAddress,AttachmentDetails)

admin.site.register(StudentEnquiry)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(ParentDetails)
admin.site.register(StudentDetail)
admin.site.register(StudentApplicationForm)
admin.site.register(Tenth)
admin.site.register(Twelth)
admin.site.register(Degree)
admin.site.register(Entrance)
admin.site.register(PermanentAddress)
admin.site.register(PresentAddress)
admin.site.register(Districts)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(AttachmentDetails)
