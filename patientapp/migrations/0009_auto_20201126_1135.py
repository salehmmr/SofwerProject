# Generated by Django 3.1.3 on 2020-11-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0008_auto_20201126_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(choices=[('Qarantine', 'قرنطینه خانگی'), ('Bastari', 'بستری در بیمارستان'), ('Normal', 'عادی'), ('Dead', 'فوت شده')], max_length=100, null=True),
        ),
    ]