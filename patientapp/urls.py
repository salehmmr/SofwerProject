from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('status/', views.statusView, name="status"),
    path('patient/', views.createPatient, name="patient"),
    path('patient/rsp/', views.getResponse, name="patient"),

]
