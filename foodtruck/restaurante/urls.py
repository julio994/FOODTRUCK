from django.urls import path
from . import views 
urlpatterns = [
    path("", views.restaurante, name="home_page"),
]
