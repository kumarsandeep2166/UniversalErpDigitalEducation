from django.urls import path
from . import views


urlpatterns=[
   
    path('feeplan_create/', views.FeesPlanTypeCreate.as_view(), name='feeplan_create'),
    path('feeplan_list/', views.FeesPlanTypeView.as_view(), name='feeplan_list'),
    path('ajax_load_list_data/', views.ajax_load_list_data, name="ajax_load_list_data"),
    #path('feecollection/', views.feecollection, name="feecollection"),
    path('plancollection/<int:id>/',views.FeePlanCreate.as_view(), name='plan_collection'),
    path('add_note/', views.add_note, name='note'),
    path('pin_toggle_note/', views.pin_toggle_note, name='pin_toggle_note'),
    path('approvecollection/<int:id>/',views.FeePlanApprove.as_view(), name='approve_collection'),
]