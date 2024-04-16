from django.shortcuts import render
from .models import Restaurante
# Create your views here.


def restaurante(request):
    rest = Restaurante.objects.all()
    return render(request,"restaurante/home.html",{"rest":rest})