from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('status/', views.statusView, name="status"),
    path('patient/', views.createPatient, name="patient"),
    path('patient/rsp/', views.getResponse, name="patientReportResponse"),
    path('all-patients/', views.PatientListView.as_view(), name='patients'),
    url(r'^patient-info/(?P<pk>\d+)$', views.PatientInfoView.as_view(), name='patient-info'),
    url(r'^all-patients/editReport/(?P<pk>\d+)$', views.editReport, name="edit-report"),

]
