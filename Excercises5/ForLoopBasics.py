# More for loops basics...
# printing multiplications from 0 to 10 

number  = int(input("Write a number: "))

for i in range(11):
    multipl = i * number 
    print(multipl)

# Countdown...

number  = int(input("Write a number: "))

if number >= 0:
    for i in range(number):
        countdown = number - i
        print(countdown)
else:
    for i in range(number -1, 0):
        countup = i + 1 
        print(countup)

#Similar as one before but with a restriction...

cuote = input("Write your favourite animal: ")
reps = int(input("How many times do you want to repeat your animal: "))

if reps <= 5:
    for i in range(reps):
        print(cuote)
else:
    print("That number of repetitions is to big, choose one number no greater than 5")


#more...

numbers = input(" Please enter four numbers: ")
a, b, c, d = numbers.split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)

question = input("Dou you want to sum the numbers you wrote? (y/n): ")

if question == "y" :
    sum = a + b + c + d
    print(sum)
else:
    print("ok.. see you next time")

#Number line...
 
side =  input("Do you want a positive or a negative number line?? :")
limitNumber = int(input("Insert a number: "))

if side.lower() == "positive":
    for i in range(limitNumber + 1):
        countup = (i-1) + 1
        print(countup)
else:
    limitNumber = limitNumber * -1
    for i in range(limitNumber + 1, 2):
        countdown = i - 1 
        print(countdown)

    #Other result for the else...
    # # for i in range(0, limitNumber):
        #     countdown = -(i) - 1 



