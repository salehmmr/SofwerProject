from django.db import models


class Symptom(models.Model):
    SYMPTOMS = (
        ('تب', 'تب'),
        ('سردرد', 'سردرد'),
        ('سرفه', 'سرفه'),
        ('بدن درد', 'بدن درد'),
        ('تنگی نفس', 'تنگی نفس'),
        ('خستگی', 'خستگی'),
        ('آبریزش بینی', 'آبریزش بینی'),

    )
    title = models.CharField(max_length=100, null=True, choices=SYMPTOMS)
    weight = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title


class Status(models.Model):
    STATUS = (
        ('Qarantine', 'قرنطینه خانگی'),
        ('Bastari', 'بستری در بیمارستان'),
        ('Normal', 'عادی'),
        ('Dead', 'فوت شده'),
    )
    Statustitle = models.CharField(max_length=100, null=True, choices=STATUS)

    def __str__(self):
        return self.Statustitle


class DiseaseStatus(models.Model):
    CONDITION = (
        ('Anfoolanza', 'آنفولانزا'),
        ('Mashkook', 'مشکوک به کرونا'),
        ('Ghatei', 'قطعی کرونا'),
    )
    DiseaseStatustitle = models.CharField(max_length=100, null=True, choices=CONDITION)
    probableWeight = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.DiseaseStatustitle + "" + self.probableWeight


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
