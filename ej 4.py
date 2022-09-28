#datos
edad = 17
edad_comp = 19
ciudad = 'Beniarjó'
ciudad_comp = 'Donosti'
#calculos
#a)
print(edad == edad_comp or ciudad == ciudad_comp)
#b)
print(ciudad == 'Castellón' or ciudad_comp == 'Castellón')
#c)
print(ciudad != 'Castellón' and ciudad_comp != 'Castellón')
#d)
print(ciudad_comp == 'Castellón' or ciudad_comp == 'Valencia' or ciudad_comp == 'Alicante')
#e)
ciudad_comp = 'Valencia'
print(ciudad_comp != 'Castellón' and ciudad_comp != 'Valencia' and ciudad_comp != 'Alicante')
print(not(ciudad_comp == 'Castellón' or ciudad_comp == 'Valencia' or ciudad_comp == 'Alicante'))
ciudad_comp = 'Teruel'
print(ciudad_comp != 'Castellón' and ciudad_comp != 'Valencia' and ciudad_comp != 'Alicante')
print(not(ciudad_comp == 'Castellón' or ciudad_comp == 'Valencia' or ciudad_comp == 'Alicante'))
#f)
print((9<edad>20) == (9<edad_comp>20))
