from django.urls import path

from . import views

urlpatterns=[
    path('stream_create/',views.StreamCreateView.as_view(),name='stream_create'),
    path('stream_list/',views.StreamListView.as_view(),name='stream_list'),
    path('coursemanagement/course_create/',views.CourseCreateView.as_view(),name='course_create'),
    path('coursemanagement/batch_create/',views.BatchCreateView.as_view(),name='batch_create'),
    path('coursemanagement/section_create/',views.SectionCreateView.as_view(),name='section_create'),

    path('coursemanagement/course_edit/<int:pk>/',views.CourseUpdateView.as_view(),name='course_edit'),
    path('coursemanagement/batch_edit/<int:pk>/',views.BatchUpdateView.as_view(),name='batch_update'),
    path('coursemanagement/section_edit/<int:pk>/',views.SectionUpdateView.as_view(),name='section_edit'),
 
    path('coursemanagement/course_list/',views.CourseListView.as_view(),name='course_list'),
    path('coursemanagement/batch_list/',views.BatchListView.as_view(),name='batch_list'),
    path('coursemanagement/section_list/',views.SectionListView.as_view(),name='section_list'),

    path('coursemanagement/course_detail/<int:pk>/',views.CourseDetailView.as_view(),name='course_detail'),
    path('coursemanagement/batch_detail/<int:pk>/',views.BatchDetailView.as_view(),name='batch_detail'),
    path('coursemanagement/section_detail/<int:pk>/',views.SectionDetailView.as_view(),name='section_detail'),

    path('coursemanagement/course_delete/<int:pk>/',views.CourseDeleteView.as_view(),name='course_delete'),
    path('coursemanagement/batch_delete/<int:pk>/',views.BatchDeleteView.as_view(),name='batch_delete'),
    path('coursemanagement/section_delete/<int:pk>/',views.SectionDeleteView.as_view(),name='section_delete'),

    path('ajax_load_course/',views.load_course,name='ajax_load_course'),
    path('ajax_load_batch/',views.load_batch,name='ajax_load_batch'),
    path('ajax_load_section/',views.load_section,name='ajax_load_section'),
    path('feetype/',views.feesmanagement,name='feesmanagement'),
    path('feetype/list',views.FeesTypeView.as_view(),name='fees_list'),
    path('feetype/feestype_delete/<int:pk>/',views.FeesTypeDeleteView.as_view(),name='fees_delete'),
    path('feetype/feestype_edit/<int:pk>/',views.FeesTypeEditView.as_view(),name='feestype_edit'),
    path('feetype/feesmanagement/',views.FeesManagementView,name='feesmanagement_create'),
    path('feetype/feesmanagement_update/<int:pk>/',views.FeesManagementSettingUpdateView.as_view(),name='feesmanagement_update'),
    path('feetype/feesmanagement_list/',views.FeesManagementSettingListView.as_view(),name='feesmanagement_list'),
    path('feetype/feesmanagement_detail/<int:pk>/',views.FeesManagementSettingDetailView.as_view(),name='feesmanagement_detail'),
    path('feetype/feesmanagement_delete/<int:pk>/',views.FeesManagementSettingDeleteView.as_view(),name='feesmanagement_delete'),
    
]