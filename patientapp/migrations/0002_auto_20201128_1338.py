# Generated by Django 3.1.3 on 2020-11-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='symptom_title',
            field=models.CharField(choices=[('تب', 'تب'), ('سردرد', 'سردرد'), ('سرفه', 'سرفه')], max_length=100, null=True),
        ),
    ]
