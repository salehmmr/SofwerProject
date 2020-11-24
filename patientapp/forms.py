from django.forms import ModelForm
from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['firstName', 'lastName', 'nationalCode', 'phoneNumber', 'symptoms']
