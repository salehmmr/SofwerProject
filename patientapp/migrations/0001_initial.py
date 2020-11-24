# Generated by Django 3.1.3 on 2020-11-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100, null=True)),
                ('nationalCode', models.CharField(max_length=100, null=True)),
                ('phoneNumber', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]