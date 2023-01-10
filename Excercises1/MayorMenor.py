#Mostrar el valor mayor entre dos números y luego su diferencia 

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 > numero2 :
    print ("El número mayor es: " + str(numero1))
elif numero1 == numero2:
    print ("Los números son iguales")
else:
    print("El número mayor es: " + str(numero2))

resta = numero1 - numero2 

segundoMensaje = "La diferencia entre ambos números es: {resta1}".format(resta1 = resta)

print(segundoMensaje)