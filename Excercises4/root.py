# trying with roots...

number =  int(input("Please write a number with value greater than 20: "))

squareRoot = number ** 0.5 

rounded =  round(squareRoot,3)

print(rounded)

# now, lets try with a circle area...

radius = int(input("Please write the radius of your circle: "))

area = 3.1416*radius**2

print(area)

#Claculating volumes...

radius = int(input("Please write the radius value of your cylinder: "))
height = int(input("Also write the cylinder's height: "))

volume = (3.1416*radius**2)*height

print(round(volume,1))
