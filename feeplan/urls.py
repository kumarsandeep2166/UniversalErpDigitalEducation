from django.urls import path
from . import views


urlpatterns=[
   
    path('feeplan_create/', views.FeesPlanTypeCreate.as_view(), name='feeplan_create'),
    path('feeplan_list/', views.FeesPlanTypeView.as_view(), name='feeplan_list'),
    path('ajax_load_list_data/', views.ajax_load_list_data, name="ajax_load_list_data"),
    path('feecollection/', views.feecollection, name="feecollection"),
    path('approvecollection/<int:id>/',views.ApproveFeePlanCreate.as_view(), name='approve_collection')
]