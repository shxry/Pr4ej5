from turtle import*

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

#movimiento
tortuga.penup()
tortuga.goto(l/2,l/2)
tortuga.pendown()
tortuga.goto(l/2,-l/2)
tortuga.goto(-l/2,-l/2)
tortuga.goto(-l/2,l/2)
tortuga.goto(l/2,l/2)
tortuga.penup()
tortuga.goto(0,-l/2)
tortuga.pendown()
tortuga.circle(l/2)

pantalla.exitonclick()
