# ¿ Quieres dividir la cuenta con tus amigos?... usa esto...

cuentaTotal = int(input("Ingresa la cuenta total: "))
totalPersonas = int(input("Ingresa cuántas personas son: "))
propina = int(input("Ingresa cuánto quieren dejar de propina en porcentaje: "))
impuesto = int(input("Ingresa el porcentaje de impuesto: "))

porcentajePropina = (propina * cuentaTotal)/100
porcentajeTaxes = (impuesto * cuentaTotal)/100

total = cuentaTotal + porcentajePropina + porcentajeTaxes

porCabeza = total/totalPersonas

print("A cada persona le toca poner: " + str(porCabeza))