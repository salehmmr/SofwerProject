# Generated by Django 3.1.3 on 2020-11-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0005_auto_20201124_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasestatus',
            name='title',
            field=models.CharField(choices=[('Anfoolanza', 'آنفولانزا'), ('Mashkook', 'مشکوک به کرونا'), ('Ghatei', 'قطعی کرونا')], max_length=100, null=True),
        ),
    ]
