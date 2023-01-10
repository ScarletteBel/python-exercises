nombre = input("Indica tu nombre: ")
edad = int(input ("Ahora ingresa tu edad: "))

edadPasada = edad - 1
edadFutura = edad + 1

mensaje = nombre + " el año pasado tenías " + str(edadPasada) + " años y el próximo año cumplirás " + str(edadFutura) + " años."

print(mensaje)