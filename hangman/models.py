from django.db import models
import random

PALABRAS = [
    "PYTHON", "DJANGO", "DOCKER", "SERVIDOR", "COMPUTADORA",
    "TECLADO", "PANTALLA", "PROGRAMACION", "VARIABLE", "FUNCION",
]

class Partida(models.Model):
    palabra = models.CharField(max_length=50)
    letras_usadas = models.CharField(max_length=100, blank=True, default="")
    intentos_restantes = models.IntegerField(default=6)
    terminada = models.BooleanField(default=False)
    ganada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def nueva_partida():
        palabra = random.choice(PALABRAS)
        return Partida.objects.create(palabra=palabra)

    def letras_usadas_lista(self):
        return list(self.letras_usadas) if self.letras_usadas else []

    def palabra_mostrada(self):
        return " ".join(
            letra if letra in self.letras_usadas_lista() else "_"
            for letra in self.palabra
        )

    def adivinar_letra(self, letra):
        letra = letra.upper()
        if self.terminada or letra in self.letras_usadas_lista():
            return

        self.letras_usadas += letra

        if letra not in self.palabra:
            self.intentos_restantes -= 1

        if all(l in self.letras_usadas_lista() for l in self.palabra):
            self.terminada = True
            self.ganada = True
        elif self.intentos_restantes <= 0:
            self.terminada = True
            self.ganada = False

        self.save()

    def __str__(self):
        return f"Partida {self.id} - {'Terminada' if self.terminada else 'En curso'}"
