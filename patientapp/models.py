from django.db import models


# Create your models here.

class Symptom(models.Model):
    SYMPTOMS = (
        ('تب', 'تب'),
        ('سردرد', 'سردرد'),
        ('سرفه', 'سرفه'),
        ('بدن درد', 'بدن درد'),
        ('تنگی نفس', 'تنگی نفس'),
        ('خستگی', 'خستگی'),
    )
    title = models.CharField(max_length=100, null=True, choices=SYMPTOMS)
    weight = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    STATUS = (
        ('قرنطینه خانگی', 'قرنطینه خانگی'),
        ('بستری در بیمارستان', 'بستری در بیمارستان'),
        ('عادی', 'عادی'),
        ('فوت شده', 'فوت شده'),
    )
    title = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.title


class DiseaseStatus(models.Model):
    CONDITION = (
        ('آنفولانزا', 'آنفولانزا'),
        ('مشکوک به کرونا', 'مشکوک به کرونا'),
        ('قطعی کرونا', 'قطعی کرونا'),
    )
    title = models.CharField(max_length=100, null=True, choices=CONDITION)
    probableWeight = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title + "" + self.probableWeight


class Patient(models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    nationalCode = models.CharField(max_length=100, null=True)
    phoneNumber = models.CharField(max_length=100, null=True)
    symptoms = models.ManyToManyField(Symptom)
    statuses = models.ManyToManyField(Status)
    diseases = models.ManyToManyField(DiseaseStatus)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Connections(models.Model):
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    phoneNumber = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
