from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def indexIni(request):
    return render(request, 'codigoh/home.html')
