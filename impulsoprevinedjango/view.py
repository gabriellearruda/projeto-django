# -*- encoding:utf-8 -*-
# Usado para encontrar urls
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from .formulario import DadosBanco

class Inicio(TemplateView):
    template_name = 'inicio.html'

class DadosAdm(TemplateView): # new
    form_class = DadosBanco
    template_name = 'dados.html'

    def get_context_data(self, **kwargs):
        context = super(DadosAdm, self).get_context_data(**kwargs)
        context['form'] = DadosBanco()
        context['action_link'] = reverse("graficos")
        return context

class Graficos(TemplateView):
    template_name = 'graficos.html'