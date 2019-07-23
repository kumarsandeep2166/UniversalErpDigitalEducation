from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('admissionfrm/',views.admissionfrm,name='admissionfrm'),
    path('applicantfrm/',views.applicantfrm,name='applicantfrm'),
    path('studentadmissionlist/',views.studentadmissionlist,name='studentadmissionlist'),
    #path('studentadmissionform/',views.studentregister,name='studentadmissionform'),
    path('studentadmissionform/',views.StudentCreateView.as_view(),name='studentadmissionform'),
    path('ajax/load-branch',views.load_branches,name='ajax_load_branch'),
    path('student-list',views.StudentListView.as_view(),name='student_list'),
    path('student_detail/<int:pk>/',views.StudentDetailView.as_view(),name='student_detail'),
    path('student_update/<int:pk>/',views.StudentUpdateView.as_view(),name='student_update'),
    path('student_delete/<int:pk>/',views.StudentDeleteView.as_view(),name='student_delete'),
    path('enquiry/',views.EnquiryListView.as_view(),name='enquiry_list'),
    #path('employee/',views.employee,name='employee'),
    # path('employee/create/',views.EmployeeCreateView.as_view(),name='employee_create'),
    # path('employee/edit/<int:pk>/',views.EmployeeUpdateView.as_view(),name='employee_edit'),
    # path('employee/',views.EmployeeListView.as_view(),name='employee_list'),
    # path('employee/delete/<int:pk>/',views.EmployeeDeleteView.as_view(),name='employee_delete'),
    # path('employee/detail/<int:pk>/',views.EmployeeDetailView.as_view(),name='employee_detail'),
    path('enroll/<int:pk>',views.EnorllmentView.as_view(),name='enrollment'),
    path('enroll_detail/<int:pk>',views.EnrollmnetViewDetail.as_view(),name='enrollment_detail'),
    path('ajax_load_enrollment/', views.ajax_load_enrollment, name='ajax_load_enrollment'),
    path('start_admission/<int:id>/', views.start_admission, name='start_admission'),


]