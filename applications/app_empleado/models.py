from django.db import models
from datetime import date
from applications.app_departamento.models import Departamento

from ckeditor.fields import RichTextField
# Create your models here.

class Abilities(models.Model) :
    ability = models.CharField('Habilidad', max_length = 30)
    
    class Meta:
        ordering = ['ability']
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'
        
    def __str__(self):
        return self.ability

class Jobs(models.Model) :
    job = models.CharField('Puesto', max_length = 50)

    class Meta:
        ordering = ['job']
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'
        
    def __str__(self):
        return self.job

class Employee(models.Model) :
    
    first_name = models.CharField('Nombre', max_length=20)
    last_name = models.CharField('Apellido', max_length=20)
    birth_date = models.DateField('Fecha de nacimiento', default='1970-1-1')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE , verbose_name='Puesto')
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Departamento')
    abilities = models.ManyToManyField(Abilities, verbose_name='Habilidades')
    observations = RichTextField('Observaciones',default='', blank=True)
    
    def calculateAge(self) :
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month,today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    
    calculateAge.short_description = 'Age'

    class Meta:
        ordering = ['-first_name', 'last_name']
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
