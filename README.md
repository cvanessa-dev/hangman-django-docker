# Hangman Django Docker

Juego del ahorcado desarrollado con Python, Django y Docker.

🚀 Demo en vivo: https://hangman-django-docker.onrender.com

## Tecnologías utilizadas

Backend: Python 3.12 & Django 5.0.6
Contenedorización: Docker & Docker Compose
Base de Datos: SQLite
Despliegue & Infraestructura: Render (Cloud Platform) & Ubuntu Server

## Características

- Selección aleatoria de palabra al iniciar cada partida
- Seguimiento de letras adivinadas y letras usadas
- Conteo de intentos restantes (6 intentos por partida)
- Detección automática de victoria o derrota
- Persistencia de cada partida en base de datos
- Interfaz visual con CSS personalizado

## 📸 Capturas del juego

### Pantalla de inicio
![Inicio](screenshots/Inicio.png)

### Partida en curso
![Juego](screenshots/Juego.png)

### Victoria
![Ganaste](screenshots/Ganar.png)

### Derrota
![Perdiste](screenshots/Perder.png)


## Cómo ejecutar el proyecto

> El proyecto fue desplegado y probado en un servidor Ubuntu Server con Docker instalado.

1. Clonar el repositorio:
git clone https://github.com/cvanessa-dev/hangman-django-docker.git
cd hangman-django-docker

2. Construir la imagen de Docker:

3. Levantar el contenedor:

4. Abrir en el navegador:
http://localhost:8000

## Estructura del proyecto
hangman-django-docker/
├── config/
├── hangman/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py

## Autora

Vanessa 
Ingeniería en Sistemas 
