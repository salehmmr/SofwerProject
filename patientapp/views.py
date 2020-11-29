from django.shortcuts import render, redirect
from django.views import generic
from . import forms
from . import models
from django.core.mail import send_mail


def send_email(email, data):
    send_mail('django test title',
              'this email is sent by Corona_Project.\n You should take care of yourself in this situation.\n\n '
              'Thanks\nlast disease:'+data,
              'sofwareengineering96@gmail.com',
              [email],
              fail_silently=False)


def new_report(data):
    first_name = data["firstName"]
    last_name = data["lastName"]
    phone_number = data["phoneNumber"]
    national_code = data["nationalCode"]
    birth_date = data['birthData']
    symptoms = data['symptoms']
    is_Available = models.Patient.objects.filter(national_code=national_code)
    if not is_Available:
        current_patient = models.Patient.objects.create(first_name=first_name,
                                                        last_name=last_name, phone_number=phone_number,
                                                        national_code=national_code, birth_date=birth_date)
        sum = 0
        for i in symptoms:
            if models.Symptom.objects.filter(symptom_title=i):
                current_symptom = models.Symptom.objects.get(symptom_title=i)
                models.PatientSymptom.objects.create(patient=current_patient, symptom=current_symptom)
                sum = sum + current_symptom.weight
        ghatei = models.DiseaseStatus.objects.get(disease_status_title="قطعی کرونا", is_System=True)
        mashkook = models.DiseaseStatus.objects.get(disease_status_title="مشکوک به کرونا", is_System=True)
        anfoolanza = models.DiseaseStatus.objects.get(disease_status_title="آنفولانزا", is_System=True)
        if sum > ghatei.probable:
            models.Status.objects.create(patient=current_patient, disease_status=ghatei)
            rsp = {'illness': ghatei.disease_status_title,
                   'patientFname': current_patient.first_name,
                   'patientLname': current_patient.last_name,
                   'patientPhone': current_patient.phone_number,
                   'patientCode': current_patient.national_code,
                   'patientBirthDate': current_patient.birth_date,
                   'patientid': current_patient.id,
                   'flag': True
                   }
        elif sum > mashkook.probable:
            models.Status.objects.create(patient=current_patient, disease_status=mashkook)
            rsp = {'illness': mashkook.disease_status_title,
                   'patientFname': current_patient.first_name,
                   'patientLname': current_patient.last_name,
                   'patientPhone': current_patient.phone_number,
                   'patientCode': current_patient.national_code,
                   'patientBirthDate': current_patient.birth_date,
                   'patientid': current_patient.id,
                   'flag': True
                   }
        else:
            models.Status.objects.create(patient=current_patient, disease_status=anfoolanza)
            rsp = {'illness': anfoolanza.disease_status_title,
                   'patientFname': current_patient.first_name,
                   'patientLname': current_patient.last_name,
                   'patientPhone': current_patient.phone_number,
                   'patientCode': current_patient.national_code,
                   'patientBirthDate': current_patient.birth_date,
                   'patientid': current_patient.id,
                   'flag': True
                   }

        return rsp

    else:
        # Current_patient = models.Patient.objects.get(nationalCode=national_code)
        # Current_patient.firstName = first_name
        # Current_patient.lastName = last_name
        # Current_patient.phoneNumber = phone_number
        # last_disease = Current_patient.diseases.last()
        # Current_patient.save()
        rsp = {'flag': False}
        return rsp


def update_patient_status(data):
    patient_id = data["patientid"]
    disease_status = data["diseaseStatus"]
    patient_status = data["patientStatus"]
    if models.Patient.objects.filter(id=patient_id):
        current_patient = models.Patient.objects.get(id=patient_id)
        current_disease = models.DiseaseStatus.objects.get(disease_status_title=disease_status, is_System=False)
        current_status = models.PatientStatus.objects.get(patient_status_title=patient_status)
        models.Status.objects.create(patient=current_patient, disease_status=current_disease,
                                     patient_status=current_status)
        return {'flag': True}
    else:
        return {'flag': False}


def edit_report(data):
    patientid = data['patientid']
    firstName = data['firstName']
    lastName = data['lastName']
    nationalCode = data['nationalCode']
    phoneNumber = data['phoneNumber']
    birthDate = data['birthDate']
    diseasestatus = data['diseaseStatus']
    patientstatus = data['patientStatus']
    symptoms = data['symptoms']

    if models.Patient.objects.filter(id=patientid):
        current_patient = models.Patient.objects.get(id=patientid)
        a = models.Status.objects.filter(patient=current_patient)
        for i in a:
            if i.disease_status.is_System:
                current_disease_system = i.disease_status
        if symptoms:
            models.PatientSymptom.objects.filter(patient=current_patient).delete()
            sum = 0
            for i in symptoms:
                current_symptom = models.Symptom.objects.get(symptom_title=i)
                sum = sum + current_symptom.weight
                models.PatientSymptom.objects.create(patient=current_patient, symptom=current_symptom)
            ghatei = models.DiseaseStatus.objects.get(disease_status_title="قطعی کرونا", is_System=True)
            mashkook = models.DiseaseStatus.objects.get(disease_status_title="مشکوک به کرونا", is_System=True)
            anfoolanza = models.DiseaseStatus.objects.get(disease_status_title="آنفولانزا", is_System=True)
            if models.PatientStatus.objects.filter(patient_status_title=patientstatus):
                current_status = models.PatientStatus.objects.get(patient_status_title=patientstatus)
                if sum > ghatei.probable:
                    models.Status.objects.create(patient=current_patient, disease_status=ghatei,
                                                 patient_status=current_status)
                    current_disease_system = ghatei
                    for i in models.Connections.objects.filter(patient=current_patient):
                        send_email(i.email, current_disease_system.disease_status_title)
                elif sum > mashkook.probable:
                    models.Status.objects.create(patient=current_patient, disease_status=mashkook,
                                                 patient_status=current_status)
                    current_disease_system = mashkook
                    for i in models.Connections.objects.filter(patient=current_patient):
                        send_email(i.email, current_disease_system.disease_status_title)
                else:
                    models.Status.objects.create(patient=current_patient, disease_status=anfoolanza,
                                                 patient_status=current_status)
                    current_disease_system = anfoolanza
            else:
                if sum > ghatei.probable:
                    models.Status.objects.create(patient=current_patient, disease_status=ghatei)
                    current_disease_system = ghatei
                elif sum > mashkook.probable:
                    models.Status.objects.create(patient=current_patient, disease_status=mashkook)
                    current_disease_system = mashkook
                else:
                    models.Status.objects.create(patient=current_patient, disease_status=anfoolanza)
                    current_disease_system = anfoolanza
        current_patient.first_name = firstName
        current_patient.last_name = lastName
        current_patient.national_code = nationalCode
        current_patient.phone_number = phoneNumber
        current_patient.birth_date = birthDate
        if models.DiseaseStatus.objects.filter(disease_status_title=diseasestatus, is_System=False) \
                and models.PatientStatus.objects.filter(patient_status_title=patientstatus):
            current_disease_user = models.DiseaseStatus.objects.get(disease_status_title=diseasestatus, is_System=False)
            current_status = models.PatientStatus.objects.get(patient_status_title=patientstatus)
            models.Status.objects.create(patient=current_patient, disease_status=current_disease_user,
                                         patient_status=current_status)
        current_patient.save()
        rsp = {
            'user-disease': current_disease_user.disease_status_title,
            'patientstatus': current_status.patient_status_title,
            'system_disease': current_disease_system.disease_status_title,
            'flaf': True
        }
        return rsp
    rsp = {
        'user-disease': 'null',
        'patientstatus': 'null',
        'system_disease': 'null',
        'flaf': False
    }
    return rsp


def make_connection(data):
    patientid = data['patientid']
    phonenumber = data['phoneNumber']
    email = data['email']
    if models.Patient.objects.filter(id=patientid):
        current_patient = models.Patient.objects.get(id=patientid)
        models.Connections.objects.create(patient=current_patient, phone_number=phonenumber, email=email)
        last_disease = ''
        for i in models.Status.objects.filter(patient=current_patient):
            last_disease = i.disease_status.disease_status_title
        if last_disease == "مشکوک به کرونا":
            send_email(email, last_disease)
        elif last_disease == "قطعی کرونا":
            send_email(email, last_disease)
        return {'flag': True}
    else:
        return {'flag': False}


# ======================

def homeView(request):
    return render(request, 'home.html')


def statusView(request):
    statuses = models.Status.objects.all()

    return render(request, 'status.html', {'statuses': statuses})


def createPatient(request):
    form1 = forms.PatientForm()
    form2 = forms.SymptomForm()
    if request.method == 'POST':
        form1 = forms.PatientForm(request.POST)
        form2 = forms.SymptomForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            myDict = dict(form1.data)
            a = myDict.get('first_name')[0]
            b = myDict.get('last_name')[0]
            c = myDict.get('national_code')[0]
            d = myDict.get('phone_number')[0]
            e = myDict.get('birth_date')[0]
            f = myDict.get('symptom_title')

            data = {
                'firstName': a,
                'lastName': b,
                'nationalCode': c,
                'phoneNumber': d,
                'birthData': e,
                'symptoms': f
            }
            rsp = new_report(data)
            if not rsp.get('flag'):
                context = {'form1': form1,
                           'form2': form2}
                return render(request, 'ErrorpatientForm.html', context)
            context = rsp
            request.session['context'] = context
            return redirect('rsp/')

    context = {'form1': form1,
               'form2': form2}
    return render(request, 'patientForm.html', context)


def getResponse(request):
    form1 = forms.DiseaseStatusForm()
    form2 = forms.PatientStatusForm()
    context = request.session['context']
    context.update({'form1': form1})
    context.update({'form2': form2})
    if request.method == 'POST':
        form1 = forms.DiseaseStatusForm(request.POST)
        form2 = forms.PatientStatusForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            myDict = dict(form1.data)
            DiseaseStatus = myDict.get('disease_status_title')[0]
            PatientStatus = myDict.get('patient_status_title')[0]

            data = {
                'diseaseStatus': DiseaseStatus,
                'patientStatus': PatientStatus
            }
            patientid = context.get('patientid')
            data.update({'patientid': patientid})
            rsp = update_patient_status(data)
            if rsp.get('flag'):
                return redirect('/')
            else:
                return render(request, 'rsp.html', context)

    return render(request, 'rsp.html', context)


class PatientListView(generic.ListView):
    model = models.Patient
    template_name = 'patient_list.html'


class PatientListConnectionView(generic.ListView):
    model = models.Patient
    template_name = 'patient_list-connection.html'


def editReport(request, pk):
    form1 = forms.PatientForm()
    form2 = forms.SymptomForm()
    form3 = forms.DiseaseStatusForm()
    form4 = forms.PatientStatusForm()
    context = {'form1': form1}
    context.update({'form2': form2})
    context.update({'form3': form3})
    context.update({'form4': form4})

    if request.method == 'POST':
        form1 = forms.PatientForm(request.POST)
        form2 = forms.SymptomForm(request.POST)
        form3 = forms.DiseaseStatusForm(request.POST)
        form4 = forms.PatientStatusForm(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            myDict = dict(form1.data)
            firstName = myDict.get('first_name')[0]
            lastName = myDict.get('last_name')[0]
            nationalCode = myDict.get('national_code')[0]
            phoneNumber = myDict.get('phone_number')[0]
            birthDate = myDict.get('birth_date')[0]
            symptoms = myDict.get('symptom_title')
            DiseaseStatus = myDict.get('disease_status_title')[0]
            PatientStatus = myDict.get('patient_status_title')[0]
            data = {
                'patientid': pk,
                'firstName': firstName,
                'lastName': lastName,
                'nationalCode': nationalCode,
                'phoneNumber': phoneNumber,
                'birthDate': birthDate,
                'symptoms': symptoms,
                'diseaseStatus': DiseaseStatus,
                'patientStatus': PatientStatus
            }
            edit_report(data)
            new_url = '/patient/patient-info/' + str(pk)
            return redirect(new_url)

    return render(request, 'editReport.html', context)


class PatientInfoView(generic.DetailView):
    model = models.Patient
    template_name = 'patient-info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # a = models.Status.objects.filter(patient_id=pk)
        # context['lastpatientstatus'] = models.Patient.objects.get(id=4).statuses.last()
        # context['lastdiseasestatus'] = models.Patient.objects.get(id=4).diseases.last()
        return context


def newConnection(request, pk):
    form1 = forms.ConnectionForm()
    context = {'form1': form1}
    if request.method == 'POST':
        form1 = forms.ConnectionForm(request.POST)
        if form1.is_valid():
            myDict = dict(form1.data)
            phoneNumber = myDict.get('phone_number')[0]
            email = myDict.get('email')[0]
            data = {
                'patientid': pk,
                'phoneNumber': phoneNumber,
                'email': email,
            }
            rsp = make_connection(data)
            if rsp.get('flag'):
                return render(request, 'new_connection_Done.html', context)
            else:
                return render(request, 'Errornew_connection.html', context)
    return render(request, 'new_connection.html', context)




