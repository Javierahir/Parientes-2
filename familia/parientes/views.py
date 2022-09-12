from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from parientes.models import Primo, Tio, Sobrino

def listar_parientes(request):
    queryset = Primo.objects.all
    diccionario = {'parientes' : queryset}
    plantillas = loader.get_template('parientes.html')
    documento_html = plantillas.render(diccionario)

    return HttpResponse (documento_html)
# Create your views here.
