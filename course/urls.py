from django.urls import path

from . import views

urlpatterns=[
    path('course/',views.CourseList.as_view(),name="course_list"),
    path('course/create/',views.CourseCreateView.as_view(),name="course_create"),
    path('course_update/<int:pk>/',views.CourseUpdateView.as_view(),name='course_update'),
    path('course_detail/<int:pk>',views.course_detail,name='course_detail'),
    path('course_delete/<int:pk>/',views.CourseDeleteView.as_view(),name='course_delete'),
    path('batch/',views.batch,name='batch'),
    path('section/',views.section,name='section'),
    path('course/course/',views.course,name='course'),
    path('stream/',views.stream,name='stream'),

]