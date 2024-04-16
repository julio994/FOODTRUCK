from django.urls import path
from . import views


urlpatterns = [
    path('<int:id_restaurante>/',views.producto , name="producto_page"),
    
]
