from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from ..app_empleado.models import Employee
# Create your views here.

class IndexView(TemplateView):
    template_name = "home/index.html"

class ListEmployees(ListView):
    template_name = "home/empleados.html"
    model = Employee