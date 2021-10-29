'''Herramientas Computacionales: El Arte de la Programación
Grupo: 201   TC1001S
Modified by:
        Léa Rodríguez Jouault A01659896
        Mauricio Juárez Sánchez A01660336'''

from random import *
from turtle import *
from freegames import path

car = path('car.gif')

# nombre diferente a las casillas
tiles = ["!", "@", "#", "¢", "$", "%", "&", "*",
         "+", "-", "º", "/", "=", ":", "?", "¡",
         "¿", "ç", "{", "]", "()", "·", "<", ">",
         "ñ", "|", "->", ";", "^", "¿?¿", "∞", "¬"] * 2

state = {'mark': None, 'Taps': 1}  # Para registrar los números de taps
hide = [True] * 64

# Para que se vea en pantalla
show = Turtle(visible=False)


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    show.undo()

    # se mostrará en pantalla el state de Taps con características definidas
    show.write(state['Taps'], font=('Arial', 30, 'normal'))

    # se le suma 1
    state['Taps'] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Central el dígito en el cuadro
        goto(x + 25.5, y + 5)
        color('red')
        # Para cetrar se utiliza también align
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    # para desplegar el total de Taps final
    if not any(hide):
        print("El Total taps es de: ", state["Taps"])
    else:
        update()
        ontimer(draw, 100)


shuffle(tiles)
setup(600, 600, 600, 0)
addshape(car)
hideturtle()
tracer(False)

show.goto(0, 200)  # ubicación del contador de Taps
show.write(state['Taps'], font=('Arial', 30, 'normal'))  # características del contador

onscreenclick(tap)
draw()
done()