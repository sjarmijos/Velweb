# Generated by Django 3.2.6 on 2021-09-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20210908_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='historia',
            field=models.TextField(verbose_name='Historia Clinica'),
        ),
    ]
