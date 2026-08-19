from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nueva/", views.nueva_partida, name="nueva_partida"),
    path("jugar/<int:partida_id>/", views.jugar, name="jugar"),
]
