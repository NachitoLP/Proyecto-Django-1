from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Employee

# Create your views here.
class ListEmployees(ListView):
    template_name = "empleados/empleados.html"
    model = Employee

class ListEmployeesByDep(ListView):
    template_name = "empleados/empleados.html"
    
    def get_queryset(self):
        departamento = self.kwargs['departamento'].title()
        queryset = Employee.objects.filter(
            department__name = departamento
        )
        return queryset