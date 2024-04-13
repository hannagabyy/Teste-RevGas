import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import Banco
from django.template import loader

# Create your views here.
def index(request):
    todos_os_bancos = Banco.objects.all()
    template = loader.get_template("bancos/listar_bancos.html")
    
    busca = request.GET.get('pesquisar-banco')
    if busca:
        todos_os_bancos = Banco.objects.filter(codigo_de_compensacao__icontains = busca)

    context = {
        "todos_os_bancos":todos_os_bancos,
    }    
    return HttpResponse(template.render(context, request))
