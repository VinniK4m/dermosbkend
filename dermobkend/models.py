from django.db import models

# Create your models here.
from django.db import models
from enum import Enum

class Medico(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    lugarNacimiento = models.CharField(max_length=30)
    lugarResidencia = models.CharField(max_length=30)
    numeroCelular = models.IntegerField()
    numeroRegistroProfesional = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Medicos'
        verbose_name_plural = 'Medicos'
        db_table = 'medicos'
        ordering = ['apellidos', '-nombres']


class Paciente(models.Model):
    nombres = models.TextField()
    apellidos = models.TextField()
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.TextField()
    lugar_residencia = models.TextField()
    numero_celular = models.IntegerField()
    correo = models.TextField()
    clave = models.CharField(max_length=15)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'pacientes'
        ordering = ['apellidos', '-nombres']

class EstadoCaso(Enum):
    CREADO = 'CREADO'
    RESERVADO = 'RESERVADO'
    SELECCIONADO = 'SELECCIONADO'
    LIBRE = 'LIBRE'

class CasoMedico(models.Model):
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    estado = EstadoCaso
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'CasoMedico'
        verbose_name_plural = 'CasosMedicos'
        db_table = 'casosmedicos'

class HistoriaClinica(models.Model):
    nombre = models.CharField(max_length=50)


class Interacciones(models.Model):
    nombre = models.CharField(max_length=50)

class Diagnostico(models.Model):
    caso = models.ForeignKey(CasoMedico, on_delete=models.PROTECT)
    fecha_diagnostico = models.DateField()
    descripcion = models.TextField()
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    aceptado = models.BooleanField()
    fecha_acepta = models.DateField()

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'
        db_table = 'diagnosticos'

class ImagenDiagnostica(models.Model):
    caso = models.ForeignKey(CasoMedico, null=True, blank=True, on_delete=models.PROTECT)
    url = models.TextField()
    descripcion = models.TextField()
    fecha_creacion = models.DateField()

    class Meta:
        verbose_name = 'ImagenDiagnostica'
        verbose_name_plural = 'ImagenesDianosticas'
        db_table = 'imagenesdianosticas'

class Tratamiento(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    detalle = models.TextField()

    class Meta:
        verbose_name = 'Tratamientos'
        verbose_name_plural = 'Tratamientos'
        db_table = 'tratamientos'

class TipoSoporte(Enum):
    PREGRADO = 'PREGRADO'
    ESPECIALIZACION = 'ESPECIALIZACION'
    CERTIFICACION = 'CERTIFICACION'
    SEMINARIO = 'SEMINARIO'
    DIPLOMADO = 'DIPLOMADO'

class Soporte(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    tipo_soporte = TipoSoporte
    descripcion = models.TextField()
    fecha_soporte = models.DateField()

    class Meta:
        verbose_name = 'Soportes'
        verbose_name_plural = 'Soportes'
        db_table = 'soportes'



