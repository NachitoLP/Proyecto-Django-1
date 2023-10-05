from django.db import models

# Create your models here.

class Departamento (models.Model) :
    name = models.CharField('Nombre' , max_length = 20)
    short_name = models.CharField('Sigla' , max_length = 5)
    active = models.BooleanField('¿Activo?' , default = False)
    floor = models.CharField('Piso' , max_length = 5)
    office = models.CharField('Oficina N°' , max_length= 10)
    
    class Meta:
        unique_together = ['name','short_name']
        
    def __str__ (self) :
        return self.name

