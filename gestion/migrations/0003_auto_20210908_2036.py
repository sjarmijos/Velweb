# Generated by Django 3.2.6 on 2021-09-09 01:36

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20210830_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='cli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas_pacientes', to='gestion.paciente', verbose_name='Paciente para la cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cosultas_medicos', to='gestion.medico', verbose_name='Médico Asignado'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_cita',
            field=models.DateField(verbose_name='Fecha de la Cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora_cita',
            field=models.TimeField(verbose_name='Hora de la Cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='id_cita',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Código de la Cita'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='id_espec',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Código de la Especialidad'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='nombre_espec',
            field=models.CharField(max_length=64, verbose_name='Nombre de la Especialidad'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='cli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historias_pacientes', to='gestion.paciente', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='historia',
            field=models.TextField(max_length=builtins.max, verbose_name='Historia Clinica'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='id_historia',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Código de la Historia Clínica'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='cedula_doc',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Cédula del Médico'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_cli',
            field=models.CharField(max_length=64, verbose_name='Apellido del Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cedula_cli',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Cédula del Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='correo_cli',
            field=models.CharField(max_length=80, verbose_name='Correo del Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccion_cli',
            field=models.CharField(max_length=64, verbose_name='Dirección del Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre_cli',
            field=models.CharField(max_length=64, verbose_name='Nombre del Paciente'),
        ),
    ]
