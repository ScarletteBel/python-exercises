
numeroGrande = int(input("Ingresa el número de mayor valor: "))
numeroChico = int(input("Ingresa el número de menor valor: "))

cuantasVecesCabe = numeroGrande/numeroChico

#mensaje =  str(numeroChico) + " cabe " + str(cuantasVecesCabe) + " en " + str(numeroGrande)

# Ejemplo de format 
# mensaje = 'Hola {nombre1} tienes {edad1} años. Te amo {nombre1}{nombre1}{nombre1}'.format(nombre1 =nombre, edad1 = edad)

mensaje = "{numeroChico1} cabe {cuantasVecesCabe1} en {numeroGrande1}".format(numeroChico1 = numeroChico, cuantasVecesCabe1 = cuantasVecesCabe, numeroGrande1 = numeroGrande)

print(mensaje)