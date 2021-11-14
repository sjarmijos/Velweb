# Generated by Django 3.2.6 on 2021-08-30 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='apellido_doc',
            field=models.CharField(max_length=64, verbose_name='Apellido del Médico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='cedula_doc',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Cedula del Médico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='correo_doc',
            field=models.CharField(max_length=80, verbose_name='Correo Electrónico del Médico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='direccion_doc',
            field=models.CharField(max_length=64, verbose_name='Dirección del Médico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='especialidades', to='gestion.especialidad', verbose_name='Especilidad del Médico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='nombre_doc',
            field=models.CharField(max_length=64, verbose_name='Nombre del Médico'),
        ),
    ]