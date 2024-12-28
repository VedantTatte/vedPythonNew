from django.urls import path
from .views import *

app_name='newAppCrud'
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('login/',login,name='login'),
]