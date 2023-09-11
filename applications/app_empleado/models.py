from django.db import models
from applications.app_departamento.models import Departamento
# Create your models here.

class Abilities(models.Model) :
    ability = models.CharField('Habilidad', max_length = 30)
    
    class Meta:
        ordering = ['ability']
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'
        
    def __str__(self):
        return self.ability

class Employee(models.Model) :
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Analista Funcional'),
        ('4', 'Otro')
    )
    
    first_name = models.CharField('Nombre', max_length=20)
    last_name = models.CharField('Apellido', max_length=20)
    job = models.CharField('Puesto', max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(Abilities)

    class Meta:
        ordering = ['-first_name', 'last_name']
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
