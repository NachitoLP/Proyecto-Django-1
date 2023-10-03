from django.contrib import admin
from django.http import HttpResponse
from django.db import models

from ckeditor.widgets import CKEditorWidget

from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas

import csv

from .models import Employee, Abilities, Jobs

# Register your models here.

admin.site.register(Abilities)
admin.site.register(Jobs)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'calculateAge',
        'job',
        'department',
    )
    search_fields = (
        'last_name',
        'first_name'
    )
    list_filter = (
        'department',
    )
    formfield_overrides = {
        models.TextField: {'widget':CKEditorWidget()},
    }
    
    def export_to_csv(self,request,queryset) :
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="datos.csv"'
        writer = csv.writer(response)

        writer.writerow(['Nombre:', 'Apellido:', 'Departamento:'])
        
        for item in queryset :
            writer.writerow([item.first_name, item.last_name, item.department])

        return response
    
    def export_to_pdf(self,request,queryset) :
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="datos.pdf"'
        
        pdf = canvas.Canvas(response, pagesize=A4)
        
        x = pdf._pagesize[0] / 2
        
        pdf.drawCentredString(x,750,"Empleados")
        pdf.setFont("Helvetica", 12)
        
        y = 700
        
        for item in queryset :
            y -= 20
            pdf.drawString(10 , y , f'Nombre: {item.first_name}')
            pdf.drawString(115 , y , f'Apellido: {item.last_name}')
            pdf.drawString(220 , y , f'Departamento: {item.department}')

        pdf.showPage()
        pdf.save()
        
        return response


    export_to_csv.short_description = "Exportar empleados seleccionados a CSV"
    export_to_pdf.short_description = "Exportar empleados seleccionados a PDF"
    
    actions = [export_to_csv,export_to_pdf]
admin.site.register(Employee,EmpleadoAdmin)