# Upper case and lower case...

word1 = input("Insert a random word: ")
word2 = input("Insert a another random word: ")

print(word1.upper())
print(word2.lower())

#Sending a message just if you follow the instructions...

name = input("What's your full name?: ")

nameLong = len(name)

if nameLong < 5:
    missingLastName = input("Please also write your last name: ")
    print("Hi " + name + " " + missingLastName + " have a great day!")
else:
    print("Hi " + name + " have a great day!")