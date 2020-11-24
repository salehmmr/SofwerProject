# Generated by Django 3.1.3 on 2020-11-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0004_remove_patient_symptoms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientsymptom',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patientsymptom',
            name='symptom',
        ),
        migrations.RemoveField(
            model_name='status',
            name='disease_status',
        ),
        migrations.RemoveField(
            model_name='status',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='status',
            name='patient_status',
        ),
        migrations.RemoveField(
            model_name='status',
            name='status_date',
        ),
        migrations.AddField(
            model_name='patient',
            name='diseases',
            field=models.ManyToManyField(to='patientapp.DiseaseStatus'),
        ),
        migrations.AddField(
            model_name='patient',
            name='statuses',
            field=models.ManyToManyField(to='patientapp.Status'),
        ),
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.ManyToManyField(to='patientapp.Symptom'),
        ),
        migrations.AddField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('قرنطینه خانگی', 'قرنطینه خانگی'), ('بستری در بیمارستان', 'بستری در بیمارستان'), ('عادی', 'عادی'), ('فوت شده', 'فوت شده')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='title',
            field=models.CharField(choices=[('تب', 'تب'), ('سردرد', 'سردرد'), ('سرفه', 'سرفه'), ('بدن درد', 'بدن درد'), ('تنگی نفس', 'تنگی نفس'), ('خستگی', 'خستگی')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='PatientStatus',
        ),
        migrations.DeleteModel(
            name='PatientSymptom',
        ),
    ]
