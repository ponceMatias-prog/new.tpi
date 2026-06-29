# Juego de la serpiente que atrapa formas geometricas
import turtle
import random
import time

# Variables
retraso = 0.1
puntaje = 0
mejor_puntaje = 0

# Crear la ventana
ventana = turtle.Screen()
ventana.title("Atrapa las formas geometricas con la serpiente.")
ventana.bgcolor("black")
ventana.setup(width=700, height=700)
ventana.tracer(0)

# Dibujar el borde
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("white")

for _ in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)

turtle.penup()
turtle.hideturtle()

# Crear la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direccion = "detenida"

# Crear la comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape(random.choice(["circle", "square", "triangle"]))
comida.color(random.choice(["yellow", "green", "tomato"]))
comida.penup()
comida.goto(20, 20)

# Crear el marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.shape("square")
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write(
    "Puntaje: 0    Mejor Puntaje: 0",
    align="center",
    font=("Courier", 24, "bold")
)
# Funciones de dirección

def mover_arriba():
    if cabeza.direccion != "abajo":
        cabeza.direccion = "arriba"

def mover_abajo():
    if cabeza.direccion != "arriba":
        cabeza.direccion = "abajo"

def mover_izquierda():
    if cabeza.direccion != "derecha":
        cabeza.direccion = "izquierda"

def mover_derecha():
    if cabeza.direccion != "izquierda":
        cabeza.direccion = "derecha"


# Función para mover la serpiente

def mover():
    if cabeza.direccion == "arriba":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    elif cabeza.direccion == "abajo":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    elif cabeza.direccion == "izquierda":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    elif cabeza.direccion == "derecha":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# Configurar controles

ventana.listen()
ventana.onkeypress(mover_arriba, "Up")
ventana.onkeypress(mover_abajo, "Down")
ventana.onkeypress(mover_izquierda, "Left")
ventana.onkeypress(mover_derecha, "Right")

# Lista para guardar los segmentos de la cola
segmentos = []
# Bucle principal del juego

while True:
    ventana.update()

    # Colisión con los bordes
    if (
        cabeza.xcor() > 290 or
        cabeza.xcor() < -290 or
        cabeza.ycor() > 240 or
        cabeza.ycor() < -240
    ):
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direccion = "detenida"

        # Ocultar todos los segmentos
        for segmento in segmentos:
            segmento.goto(1000, 1000)

        segmentos.clear()

        puntaje = 0
        retraso = 0.1

        marcador.clear()
        marcador.write(
            f"Puntaje: {puntaje}    Mejor Puntaje: {mejor_puntaje}",
            align="center",
            font=("Courier", 24, "bold")
        )

    # Colisión con la comida
    if cabeza.distance(comida) < 20:

        x = random.randint(-280, 280)
        y = random.randint(-230, 230)
        comida.goto(x, y)

        comida.shape(random.choice(["circle", "square", "triangle"]))
        comida.color(random.choice(["yellow", "green", "red", "blue", "orange"]))

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("gray")
        nuevo_segmento.penup()

        segmentos.append(nuevo_segmento)

        retraso -= 0.001

        puntaje += 10

        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje

        marcador.clear()
        marcador.write(
            f"Puntaje: {puntaje}    Mejor Puntaje: {mejor_puntaje}",
            align="center",
            font=("Courier", 24, "bold")
        )
# Mover los segmentos desde el último hasta el primero
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    # El primer segmento sigue a la cabeza
    if len(segmentos) > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    # Mover la cabeza
    mover()

    # Comprobar si la cabeza choca con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direccion = "detenida"

            for s in segmentos:
                s.goto(1000, 1000)

            segmentos.clear()

            puntaje = 0
            retraso = 0.1

            marcador.clear()
            marcador.write(
                f"Puntaje: {puntaje}    Mejor Puntaje: {mejor_puntaje}",
                align="center",
                font=("Courier", 24, "bold")
            )

    time.sleep(retraso)
   # Mantener la ventana abierta al cerrar el juego
ventana.mainloop()
#No se pueden chocar ni paredes o cola que muere.
#Se utilizo videos de programacion de videojuegos de internet para hacer mejor este juego.
