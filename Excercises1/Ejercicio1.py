edad = input("Ingresa tu edad, porfa: ")

for i in range( int(edad) +1 ):
    print("Esto es una cuenta regresiva", int (edad) -i )

#Lo mismo pero en función 

def funcionRegresiva(edadFuncion):
    
    edadFuncion = input("Ingresa tu edad, porfa: ")
    
    for i in range( int(edadFuncion) +1 ):
        print("Esto es una cuenta regresiva", int (edadFuncion) -i )

print(funcionRegresiva(3))
