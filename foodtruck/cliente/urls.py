from django.urls import path
from . import views 
urlpatterns = [
    path("", views.cliente, name="cliente_pag"),
]
