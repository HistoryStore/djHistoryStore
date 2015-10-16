# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from compras.models import List

def indice(request):

    return HttpResponse("Hola mundo. Este es el índice de los graficos")