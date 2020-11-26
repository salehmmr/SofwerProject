# Generated by Django 3.1.3 on 2020-11-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DiseaseStatustitle', models.CharField(choices=[('Anfoolanza', 'آنفولانزا'), ('Mashkook', 'مشکوک به کرونا'), ('Ghatei', 'قطعی کرونا')], max_length=100, null=True)),
                ('probableWeight', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statustitle', models.CharField(choices=[('Qarantine', 'قرنطینه خانگی'), ('Bastari', 'بستری در بیمارستان'), ('Normal', 'عادی'), ('Dead', 'فوت شده')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('تب', 'تب'), ('سردرد', 'سردرد'), ('سرفه', 'سرفه'), ('بدن درد', 'بدن درد'), ('تنگی نفس', 'تنگی نفس'), ('خستگی', 'خستگی')], max_length=100, null=True)),
                ('weight', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100, null=True)),
                ('nationalCode', models.CharField(max_length=100, null=True)),
                ('phoneNumber', models.CharField(max_length=100, null=True)),
                ('diseases', models.ManyToManyField(to='patientapp.DiseaseStatus')),
                ('statuses', models.ManyToManyField(to='patientapp.Status')),
                ('symptoms', models.ManyToManyField(to='patientapp.Symptom')),
            ],
        ),
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patientapp.patient')),
            ],
        ),
    ]
