from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('payment',views.pay,name='payment'),
    path('success',views.success,name='success'),
    path('rz',views.rz,name='rz')
]