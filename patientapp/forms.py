from django.forms import ModelForm, forms
from . import models


class PatientForm(ModelForm):
    class Meta:
        model = models.Patient
        fields = ['firstName', 'lastName', 'nationalCode', 'phoneNumber', 'symptoms']


class DiseaseStatusForm(ModelForm):
    class Meta:
        model = models.DiseaseStatus
        fields = ['DiseaseStatustitle']


class StatusForm(ModelForm):
    class Meta:
        model = models.Status
        fields = ['Statustitle']
