import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import Banco
from django.template import loader

# Create your views here.
def index(request):
    todos_os_bancos = Banco.objects.all()
    template = loader.get_template("bancos/index.html")
    context = {
        "todos_os_bancos":todos_os_bancos,
    }
    return HttpResponse(template.render(context, request))

def resultado(request, banco_id):
    response = "You're looking at the results of banco %s."
    return HttpResponse(response % banco_id)