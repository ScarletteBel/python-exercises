# Counting how many pizza slices do we still have 

print("Let´s see how many pizzas do u still have...")

totalPizza = int(input("How many slices u have when nobody has ate yet?: "))
eatenSlices = int(input("After a few minutes...how many slices have been eaten?: "))

resta = totalPizza - eatenSlices 

result = ("You still have" + " " + str(resta) + " " + "slices!")

print(result)
