# still playing with strings...

phrase = input("Write a fragment of your favorite song: ")

numbersString = len(phrase)

print("Think in a range of numbers between 1 to " + str(numbersString)) 
rangeInitial = input("Write the initial nUmber of the range you have in mind: ")
rangeFinal = input("Write the final number of the range you have in mind: ")

lettersInRange = phrase[int(rangeInitial) : int(rangeFinal)]

print(lettersInRange)


