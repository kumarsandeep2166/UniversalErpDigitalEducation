from django.urls import path

from . import views

urlpatterns=[
    path('semestar_create/',views.SemestarCreateView.as_view(),name="semestar_create"),
    path('semestar/', views.SemestarList.as_view(), name="semestar-list"),
    path('subject_create/',views.SubjectCreateView.as_view(),name="subject_create"),
    path('subject/', views.SubjectList.as_view(), name="subject-list"),
    path('subject_teacher/', views.SubjectTeacherList.as_view(), name="subject_teacher-list"),
    path('ajax_load_sem/', views.ajax_load_sem, name='ajax_load_sem'),
    path('assign_subject_teacher/', views.SubjectTeacherCreateView.as_view(), name='assign_subject_teacher'),
    path('ajax_load_subject/', views.ajax_load_subject, name="ajax_load_subject"),
    path('subject_teacher_update/<int:pk>', views.StudentTeacherUpdateView.as_view(), name="subject_teacher_update"),
    path('subject_teacher_delete/<int:pk>/', views.StudentTeacherDeleteView.as_view(), name="subject_teacher_delete"),
    #path('lesson_plan/', views.LessonPlanCreateView.as_view(), name="subject_lesson_plan"),
    path('attendance/', views.attendance, name="attendance"),
    path('ajax_load_attendance/', views.ajax_load_attendance, name="ajax_load_attendance"),
    path('save_attendance/', views.save_attendance, name="save_attendance"),
]