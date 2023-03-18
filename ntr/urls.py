from django.urls import path

from ntr.views import *

app_name='ntr'

urlpatterns=[
    path('temper/',temper,name='temper'),
    path('aadhi/',aadhi,name='aadhi'),
]