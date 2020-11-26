from django.shortcuts import render, redirect
from . import forms
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
            a = models.Symptom.objects.get(id=i)
            p.symptoms.add(a)
            sum = sum + int(a.weight)

        a = models.DiseaseStatus.objects.get(DiseaseStatustitle="Ghatei")
        b = models.DiseaseStatus.objects.get(DiseaseStatustitle="Mashkook")
        c = models.DiseaseStatus.objects.get(DiseaseStatustitle="Anfoolanza")
        if sum > int(a.probableWeight):
            p.diseases.add(a)
            rsp = {'illness': "قطعی کرونا",
                   'patientid': p.id,
                   'patientFname': p.firstName,
                   'patientLname': p.lastName,
                   'patientPhone': p.phoneNumber,
                   'patientCode': p.nationalCode
                   }
        elif sum > int(b.probableWeight):
            p.diseases.add(b)
            rsp = {'illness': "مشکوک به کرونا",
                   'patientid': p.id,
                   'patientFname': p.firstName,
                   'patientLname': p.lastName,
                   'patientPhone': p.phoneNumber,
                   'patientCode': p.nationalCode
                   }
        else:
            p.diseases.add(c)
            rsp = {'illness': "آنفولانزا",
                   'patientid': p.id,
                   'patientFname': p.firstName,
                   'patientLname': p.lastName,
                   'patientPhone': p.phoneNumber,
                   'patientCode': p.nationalCode
                   }
        return rsp

    else:
        return {'illness': "Unkown",
                'patientid': "",
                'patientFname': "",
                'patientLname': "",
                'patientPhone': "",
                'patientCode': ""
                }


def update_patient_status(data):
    patient_id = data["patientid"]
    disease_status = data["DiseaseStatus"]
    patient_status = data["PatientStatus"]
    current_patient = models.Patient.objects.get(id=patient_id)
    disease = models.DiseaseStatus.objects.get(DiseaseStatustitle=disease_status)
    current_patient.diseases.add(disease)
    status = models.Status.objects.get(Statustitle=patient_status)
    current_patient.statuses.add(status)
    return "DONE"


# ======================

def homeView(request):
    return render(request, 'home.html')


def statusView(request):
    statuses = models.Status.objects.all()

    return render(request, 'status.html', {'statuses': statuses})


def createPatient(request):
    form = forms.PatientForm()
    if request.method == 'POST':
        form = forms.PatientForm(request.POST)
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
            if rsp.get('illness') == 'Unkown':
                context = {'form': form}
                return render(request, 'ErrorpatientForm.html', context)
            context = rsp
            request.session['context'] = context
            return redirect('rsp/')

    context = {'form': form}
    return render(request, 'patientForm.html', context)


def getResponse(request):
    form1 = forms.DiseaseStatusForm()
    form2 = forms.StatusForm()
    context = request.session['context']
    context.update({'form1': form1})
    context.update({'form2': form2})
    if request.method == 'POST':
        form1 = forms.DiseaseStatusForm(request.POST)
        form2 = forms.StatusForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print(form1.data)
            myDict = dict(form1.data)
            DiseaseStatus = myDict.get('DiseaseStatustitle')[0]
            PatientStatus = myDict.get('Statustitle')[0]

            data = {
                'DiseaseStatus': DiseaseStatus,
                'PatientStatus': PatientStatus
            }
            a = context.get('patientid')
            data.update({'patientid': a})
            rsp = update_patient_status(data)
            print(rsp)

    return render(request, 'rsp.html', context)

    # return render(request, 'rsp.html', )