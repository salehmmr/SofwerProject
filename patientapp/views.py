from django.shortcuts import render, redirect
from django.views import generic
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

        a = models.DiseaseStatus.objects.get(DiseaseStatustitle="Ghatei", is_System=True)
        b = models.DiseaseStatus.objects.get(DiseaseStatustitle="Mashkook", is_System=True)
        c = models.DiseaseStatus.objects.get(DiseaseStatustitle="Anfoolanza", is_System=True)
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
    disease = models.DiseaseStatus.objects.get(DiseaseStatustitle=disease_status, is_System=False)
    current_patient.diseases.add(disease)
    status = models.Status.objects.get(Statustitle=patient_status)
    current_patient.statuses.add(status)
    return "DONE"


def edit_report(data):
    patientid = data['patientid']
    firstName = data['firstName']
    lastName = data['lastName']
    nationalCode = data['nationalCode']
    phoneNumber = data['phoneNumber']
    diseasestatus = data['diseasestatus']
    patientstatus = data['patientstatus']
    symptoms = data['symptoms']
    current_patient = models.Patient.objects.get(id=patientid)
    if symptoms:
        models.Patient.objects.get(id=patientid).symptoms.clear()
        sum = 0
        for i in symptoms:
            current_symptom = models.Symptom.objects.get(id=i)
            sum = sum + int(current_symptom.weight)
            current_patient.symptoms.add(current_symptom)
        if sum > 10:
            current_DiseaseStatus = models.DiseaseStatus.objects.get(DiseaseStatustitle="Ghatei", is_System=True)
            current_patient.diseases.add(current_DiseaseStatus)
        elif sum > 5:
            current_DiseaseStatus = models.DiseaseStatus.objects.get(DiseaseStatustitle="Mashkook", is_System=True)
            current_patient.diseases.add(current_DiseaseStatus)
        else:
            current_DiseaseStatus = models.DiseaseStatus.objects.get(DiseaseStatustitle="Anfoolanza", is_System=True)
            current_patient.diseases.add(current_DiseaseStatus)

    current_patient.firstName = firstName
    current_patient.lastName = lastName
    current_patient.phoneNumber = phoneNumber
    current_patient.nationalCode = nationalCode
    current_disease = models.DiseaseStatus.objects.get(DiseaseStatustitle=diseasestatus, is_System=False)
    current_status = models.Status.objects.get(Statustitle=patientstatus)
    current_patient.diseases.add(current_disease)
    current_patient.statuses.add(current_status)
    current_patient.save()


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


class PatientListView(generic.ListView):
    model = models.Patient
    template_name = 'patient_list.html'


def editReport(request, pk):
    form1 = forms.PatientForm()
    form2 = forms.DiseaseStatusForm()
    form3 = forms.StatusForm()
    context = {'form1': form1}
    context.update({'form2': form2})
    context.update({'form3': form3})

    if request.method == 'POST':

        form1 = forms.PatientForm(request.POST)
        form2 = forms.DiseaseStatusForm(request.POST)
        form3 = forms.StatusForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            myDict = dict(form1.data)
            firstName = myDict.get('firstName')[0]
            lastName = myDict.get('lastName')[0]
            nationalCode = myDict.get('nationalCode')[0]
            phoneNumber = myDict.get('phoneNumber')[0]
            symptoms = myDict.get('symptoms')
            DiseaseStatus = myDict.get('DiseaseStatustitle')[0]
            PatientStatus = myDict.get('Statustitle')[0]
            data = {
                'patientid': pk,
                'firstName': firstName,
                'lastName': lastName,
                'nationalCode': nationalCode,
                'phoneNumber': phoneNumber,
                'symptoms': symptoms,
                'diseasestatus': DiseaseStatus,
                'patientstatus': PatientStatus
            }
            edit_report(data)
            a = '/patient/patient-info/' + str(pk)
            return redirect(a)

    return render(request, 'editReport.html', context)


class PatientInfoView(generic.DetailView):
    model = models.Patient
    template_name = 'patient-info.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lastpatientstatus'] = models.Patient.objects.get(id=4).statuses.last()
        context['lastdiseasestatus'] = models.Patient.objects.get(id=4).diseases.last()
        return context
