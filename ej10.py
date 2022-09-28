from turtle import*
from math import*

#setup pantalla
pantalla = Screen()
DIMX=400
DIMY=200
pantalla.setup(DIMX+25, DIMY+25)
pantalla.screensize(DIMX,DIMY)

#asignacion tortuga
tortuga=Turtle()

#datos
l = int(input('Dame el lado del cuadrado'))
a = int(input('Dame la coordenada x del punto'))
b = int(input('Dame la coordenada y del punto'))
#calculo radio
l2 = l/2
radio =int(sqrt(l2**2 + l2**2))
#movimiento cuadrado
tortuga.write('(0,0)')
tortuga.dot(0)
tortuga.penup()
tortuga.goto(l2,l2)
tortuga.pendown()
tortuga.pencolor('red')
tortuga.goto(l2,-l2)
tortuga.goto(-l2,-l2)
tortuga.goto(-l2,l2)
tortuga.goto(l2,l2)

#movimiento circulo
tortuga.penup()
tortuga.goto(0,-radio)
tortuga.pendown()
tortuga.pencolor('blue')
tortuga.circle(radio)

#condicionales punto
tortuga.penup()
tortuga.goto(a,b)
tortuga.pendown()
if a>-l2 and a<l2 and b>-l2 and b<l2  :
    tortuga.pencolor('red')
else:
    if a>-radio and a<radio and b>-radio and a<radio:
        tortuga.pencolor('blue')
    else:
        tortuga.pencolor('green')

tortuga.dot(0)
  
        


    


pantalla.exitonclick()
