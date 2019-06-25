from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('admissionfrm/',views.admissionfrm,name='admissionfrm'),
    path('applicantfrm/',views.applicantfrm,name='applicantfrm'),
    path('studentadmissionlist/',views.studentadmissionlist,name='studentadmissionlist'),
    path('studentadmissionform/',views.studentregister,name='studentadmissionform'),
    path('ajax/load-branch',views.load_branches,name='ajax_load_branch'),
    path('student-list',views.StudentListView.as_view(),name='student_list'),
    path('<int:pk>/student-detail/',views.StudentListView.as_view(),name='student_detail'),
]