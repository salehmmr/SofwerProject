from django.shortcuts import render, redirect
from .models import *
from .forms import PatientForm
from . import models


def new_report(data):
    first_name = data["firstName"]
    last_name = data["lastName"]
    phone_number = data["phoneNumber"]
    national_code = data["nationalCode"]
    symptoms = data['symptoms']
    is_Available = models.Patient.objects.filter(nationalCode=national_code)
    if not is_Available:
        p = models.Patient.objects.create(firstName=first_name, lastName=last_name, phoneNumber=phone_number,
                                          nationalCode=national_code)
        sum = 0
        for i in symptoms:
            a = Symptom.objects.get(id=i)
            p.symptoms.add(a)
            sum = sum + int(a.weight)
        avg = sum / len(symptoms)
        if avg > 5:
            rsp = {'illness': "Ghatei"}
        elif avg > 3:
            rsp = {'illness': "Mashkook"}
        else:
            rsp = {'illness': "Anfoolanza"}

        return rsp

    else:
        return {'illness': "Unkown"}


# ======================

def homeView(request):
    return render(request, 'home.html')


def statusView(request):
    statuses = Status.objects.all()

    return render(request, 'status.html', {'statuses': statuses})


def createPatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            myDict = dict(form.data)
            a = myDict.get('firstName')[0]
            b = myDict.get('lastName')[0]
            c = myDict.get('nationalCode')[0]
            d = myDict.get('phoneNumber')[0]
            e = myDict.get('symptoms')

            data = {
                'firstName': a,
                'lastName': b,
                'nationalCode': c,
                'phoneNumber': d,
                'symptoms': e
            }
            rsp = new_report(data)
            context = rsp
            return render(request, 'rsp.html', context)

    context = {'form': form}
    return render(request, 'patientForm.html', context)
