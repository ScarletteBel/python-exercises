#Para saber cuantas horas, minutos y segundos faltan...

dias = int(input("Ingresa la cantidad de días: "))

horas = dias * 24
minutos = horas * 60
segundos = minutos * 60 

respuesta = str(dias) + " días es igual a " + str(horas) + " horas" + ", " + str(minutos) + " minutos, " + str(segundos) + " segundos"

print(respuesta)