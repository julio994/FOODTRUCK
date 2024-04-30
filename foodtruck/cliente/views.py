from django.shortcuts import render, HttpResponse
from .models import Cliente
def cliente(request):
    client= Cliente.objects.all()
    return render(request,"cliente/cliente.html",{"client":client})


