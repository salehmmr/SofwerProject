from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homeView, name="home"),
    path('status/', views.statusView, name="status"),
    path('patient/', views.createPatient, name="patient"),
    path('patient/rsp/', views.getResponse, name="patientReportResponse"),
    path('all-patients/', views.PatientListView.as_view(), name='patients'),
    path('all-patients-connection/', views.PatientListConnectionView.as_view(), name='patients-connection'),
    url(r'^connection-patient/(?P<pk>\d+)$', views.newConnection, name="connection-patient"),
    url(r'^edit-report/(?P<pk>\d+)$', views.editReport, name="edit-report"),
    url(r'^patient-info/(?P<pk>\d+)$', views.PatientInfoView.as_view(), name='patient-info'),

]
