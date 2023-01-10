#Veamos si el número está dentro de rango...

numeroLimite = int(input("Ingresa el número límite: "))
numeroComparar = int(input("Ingresa el número a evaluar: "))

mensaje1 = "El número {numeroComparar1} se encuentra en el rango".format(numeroComparar1 = numeroComparar)
mensaje2 = "El número {numeroComparar1} está en el límite".format(numeroComparar1 = numeroComparar)
mensaje3 = "El número {numeroComparar1} se excede del límite".format(numeroComparar1 = numeroComparar)


if numeroComparar < numeroLimite:
    print(mensaje1)
elif numeroLimite == numeroComparar:
    print(mensaje2)
else:
    print(mensaje2)

