from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError('La fecha de inicio debe ser anterior a la fecha de fin')     
        return super().clean()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre
    
    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError('La fecha de nacimiento no puede ser posterior al dia actual.')
        if date.today().year - self.fecha_nacimiento.year < 18:
            raise ValidationError('El estudiante debe tener al menos 18 años.')
        return super().clean()

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"Estudiante: {self.estudiante} - Curso: {self.curso}"
    
    def clean(self):
        if self.fecha_inscripcion > self.curso.fecha_fin:
            raise ValidationError('El curso al que se inscribe ya ha finalizado.')
        if self.fecha_inscripcion > date.today():
            raise ValidationError('La fecha de inscripcion no puede ser posterior al dia actual.')
        return super().clean()
        