from django.shortcuts import render, redirect, get_object_or_404
from .models import Partida

def inicio(request):
    return render(request, "hangman/inicio.html")

def nueva_partida(request):
    partida = Partida.nueva_partida()
    return redirect("jugar", partida_id=partida.id)

def jugar(request, partida_id):
    partida = get_object_or_404(Partida, id=partida_id)

    if request.method == "POST":
        letra = request.POST.get("letra", "")
        if letra:
            partida.adivinar_letra(letra)
        return redirect("jugar", partida_id=partida.id)

    contexto = {
        "partida": partida,
        "palabra_mostrada": partida.palabra_mostrada(),
        "letras_usadas": partida.letras_usadas_lista(),
    }
    return render(request, "hangman/jugar.html", contexto)
