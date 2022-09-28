#datos

kg = float(input('Dame tu peso en kg'))
m = float(input('Dame tu estatura en m'))

#calcular IMC
imc = float(round(kg/(m**2),2))
imc2 = str(imc)

#calcular el estado del peso del imc de la persona

if imc>= 40:
     estado = str('obesidad morbida')
else :
    if imc>=30 :
        estado = str('obesidad')
    else :
        if imc>=25:
            estado = str('sobrepeso')
        else : 
            if imc>=18.5 :
                estado = str('peso normal')
            else :
                estado = str('bajo peso')

#imprimir el resultado

print('Tu IMC es: ' + imc2 +'. Tu estado corporal es: ' + estado)
