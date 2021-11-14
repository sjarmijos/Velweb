from django.db import models
from django.db.models.base import Model

# Create your models here.

class Especialidad(models.Model):
    id_espec=models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Código Especialidad")
    nombre_espec=models.CharField(max_length=64, verbose_name="Nombre de la Especialidad")

    def __str__(self):
        return f"{self.id_espec}: {self.nombre_espec}"

class Medico(models.Model):
    cedula_doc=models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Cédula del Médico")
    nombre_doc=models.CharField(max_length=64, verbose_name="Nombre del Médico")
    apellido_doc=models.CharField(max_length=64, verbose_name="Apellido del Médico")
    direccion_doc=models.CharField(max_length=64, verbose_name="Dirección del Médico")
    especialidad=models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name="especialidades", verbose_name="Especilidad del Médico")
    correo_doc=models.CharField(max_length=80, verbose_name="Correo Electrónico del Médico")
    
    def __str__(self):
        return f"{self.cedula_doc} {self.nombre_doc} {self.apellido_doc} {self.especialidad}"


class Paciente(models.Model):
    cedula_cli=models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Cédula del Paciente")
    nombre_cli=models.CharField(max_length=64, verbose_name="Nombre del Paciente")
    apellido_cli=models.CharField(max_length=64, verbose_name="Apellido del Paciente")
    direccion_cli=models.CharField(max_length=64, verbose_name="Dirección del Paciente")
    correo_cli=models.CharField(max_length=80, verbose_name="Correo del Paciente")

    def __str__(self):
        return f"{self.cedula_cli} {self.nombre_cli} {self.apellido_cli}"

class Cita(models.Model):
    id_cita=models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Código de la Cita")
    cli=models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="consultas_pacientes", verbose_name="Paciente para la cita")
    fecha_cita=models.DateField(verbose_name="Fecha de la Cita")
    hora_cita=models.TimeField(verbose_name="Hora de la Cita")
    doc=models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="cosultas_medicos", verbose_name="Médico Asignado")
    
    def __str__(self):
        return f"{self.id_cita}:{self.fecha_cita} {self.hora_cita} {self.doc} {self.cli}"

class Historial(models.Model):
    id_historia=models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Código de la Historia Clínica")
    cli=models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="historias_pacientes", verbose_name="Paciente")
    historia=models.TextField(verbose_name="Historia Clinica")

    def __str__(self):
        return f"{self.id_historia}: {self.cli} {self.historia}"
        