from django.shortcuts import render
from django.views.generic import CreateView

from gestion.forms import RegistroUsuarioForm


class RegistroUsuarioVista(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'registro/registro.html'