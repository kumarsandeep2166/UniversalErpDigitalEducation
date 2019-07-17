from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.index,name='fees'),
    path('home/<fee_id>',views.homefee,name='homefees'),
]