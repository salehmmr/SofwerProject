from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Patient)
admin.site.register(Status)
admin.site.register(PatientSymptom)
admin.site.register(Symptom)
admin.site.register(DiseaseStatus)
admin.site.register(Connections)
admin.site.register(PatientStatus)