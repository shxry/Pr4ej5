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
centroX = int(input('Dame las coordenada X del centro del circulo'))
centroY = int(input('Dame las coordenada Y del centro del circulo'))
radio = int(input('Dame el radio del circulo'))
centroX1 = str(centroX)
centroY1 = str(centroY)
radio1 = str(radio)
#movimiento
tortuga.penup()
tortuga.goto(centroX, centroY)
tortuga.write('(' + centroX1 + ',' + centroY1 + ')')
tortuga.pendown()
tortuga.setx(radio+centroX)
tortuga.write('radio = ' + radio1)
tortuga.goto(centroX, centroY)
tortuga.penup()
tortuga.sety(-radio+centroY)
tortuga.pendown()
tortuga.circle(radio)
pantalla.exitonclick()
