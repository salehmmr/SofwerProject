from datetime import date
from django.db import models
from django.utils.timezone import *
from django.urls import reverse


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    national_code = models.CharField(max_length=15)
    birth_date = models.DateField(default=date.today)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('edit-report', args=[str(self.id)])

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Symptom(models.Model):
    SYMPTOMS = (
        ('تب', 'تب'),
        ('سر درد', 'سر درد'),
        ('سرفه خشک', 'سرفه خشک'),
        ('خستگی', 'خستگی'),
        ('تنگی نفس', 'تنگی نفس'),
        ('آبریزش بینی', 'آبریزش بینی'),
        ('گلو درد', 'گلو درد')
    )
    symptom_title = models.CharField(max_length=100, null=True, choices=SYMPTOMS)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.symptom_title


class PatientSymptom(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)


class PatientStatus(models.Model):
    PATIENTSTATUS = (
        ('قرنطینه', 'قرنطینه'),
        ('بستری در بیمارستان', 'بستری در بیمارستان'),
        ('عادی', 'عادی'),
        ('فوت شده', 'فوت شده'),
    )
    patient_status_title = models.CharField(max_length=100, null=True, choices=PATIENTSTATUS)

    def __str__(self):
        return self.patient_status_title


class DiseaseStatus(models.Model):
    CONDITION = (
        ('آنفولانزا', 'آنفولانزا'),
        ('مشکوک به کرونا', 'مشکوک به کرونا'),
        ('قطعی کرونا', 'قطعی کرونا'),
    )
    disease_status_title = models.CharField(max_length=100, null=True, choices=CONDITION)
    probable = models.IntegerField(default=1)
    is_System = models.BooleanField(default=False)

    def __str__(self):
        return self.disease_status_title + " " + str(self.is_System)


class Connections(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)


class Status(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    patient_status = models.ForeignKey(PatientStatus, on_delete=models.CASCADE, null=True)
    disease_status = models.ForeignKey(DiseaseStatus, on_delete=models.CASCADE)
    status_date = models.DateField(default=date.today)
