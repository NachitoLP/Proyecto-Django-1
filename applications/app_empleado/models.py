from django.db import models
from applications.app_departamento.models import Departamento
# Create your models here.

class Empleado(models.Model) :
    
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

    class Meta:
        ordering = ['first_name']
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
