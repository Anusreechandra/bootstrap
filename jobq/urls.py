
# from typing import NamedTuple
from django.urls import path
from django.urls.conf import include
from . import views
app_name="jobq"
urlpatterns =[
             path('home',views.home,name='home'),
             path('login',views.login,name='login'),
             path('reg',views.reg,name='reg'),
             path('contact',views.contact,name='contact'),

]