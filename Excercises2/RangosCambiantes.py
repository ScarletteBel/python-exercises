#Indicar si el número está dentro de rango, por debajo o por arriba...

limiteInferior = int(input("Ingresa el limite inferior: "))
limiteSuperior = int(input("Ingresa el limite superior: "))
numeroComparar = int(input("Ingresa el numero a evaluar: "))

if numeroComparar < limiteInferior:
    print("El valor que ingresaste está por debajo del rango")
elif numeroComparar > limiteSuperior:
    print("El valor que ingresaste está por encima del rango")
else:
    print("El número que ingresaste está dentro del rango")