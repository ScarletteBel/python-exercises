# #Practicing basic For loop excercises....

cuote = input("Write a nice cuote you would like to remeber many times: ")

for i in range(8):
    print(cuote)

# #Trying a little bit different..

cuote = input("Write a nice cuote you would like to remeber many times: ")
reps = int(input("How many times do you want to repeat your cuote?: "))

for i in range(reps):
    print(cuote)

# #One more...

word = input("Insert a word: ")

for i in word:
    print(i)

#...
favouriteAnimal = input("Write your favourite animal: ")
reps = int(input("How many times do you want to repeat your animal?: "))

for i in range(reps):
    for i in favouriteAnimal:
        print(i)

    print(i)


