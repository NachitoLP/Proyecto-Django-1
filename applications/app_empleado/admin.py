from django.contrib import admin
from .models import Employee, Abilities

# Register your models here.

admin.site.register(Abilities)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'department'
    )

admin.site.register(Employee,EmpleadoAdmin)