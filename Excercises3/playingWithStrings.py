# Just counting...

course = input("Insert the name of your favourite course: ")

numberOfLetters = len(course)

print(numberOfLetters)

#Let's know a little about you...

name = input("What's your name: ")
lastName =  input("What's your last name: ")
favoriteFood = input("What's your favourite food: ")

print("Hi! My name is " + name + " " + lastName + " and my favorite food is " + favoriteFood)

#Little corrections...

name = input("What's your name?: ")
lastName =  input("What's your last name?: ")
country = input("Where are you from?: ")

message = "You are " + name.capitalize() + lastName.capitalize() + " from " + country.capitalize()

print(message)
