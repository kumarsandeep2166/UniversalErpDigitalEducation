from django.urls import path

from . import views

urlpatterns=[
    path('semestar_create/',views.SemestarCreateView.as_view(),name="semestar_create"),
    path('semestar/', views.SemestarList.as_view(), name="semestar-list"),
    path('subject_create/',views.SubjectCreateView.as_view(),name="subject_create"),
    path('subject/', views.SubjectList.as_view(), name="subject-list"),
    path('ajax_load_sem/', views.ajax_load_sem, name='ajax_load_sem'),
    path('assign_subject_teacher/', views.SubjectTeacherCreateView.as_view(), name='assign_subject_teacher'),
    path('ajax_load_subject/', views.ajax_load_subject, name="ajax_load_subject"),
]