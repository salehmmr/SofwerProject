from django.forms import ModelForm
from . import models


class PatientForm(ModelForm):
    class Meta:
        model = models.Patient
        fields = ['first_name', 'last_name', 'phone_number', 'national_code', 'birth_date']


class SymptomForm(ModelForm):
    class Meta:
        model = models.Symptom
        fields = ['symptom_title']


class DiseaseStatusForm(ModelForm):
    class Meta:
        model = models.DiseaseStatus
        fields = ['disease_status_title']


class PatientStatusForm(ModelForm):
    class Meta:
        model = models.PatientStatus
        fields = ['patient_status_title']


class ConnectionForm(ModelForm):
    class Meta:
        model = models.Connections
        fields = ['phone_number', 'email']