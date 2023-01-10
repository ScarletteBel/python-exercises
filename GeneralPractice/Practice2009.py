# Character pyramid...

noLevel = int(input("How many levels do you want your pyramid? "))
figure = input("Inset the character do you want? ")

for i in range (noLevel):
    #levelCont = " " * (noLevel - i), figure + i, " " * (noLevel - i)
    levelCont = " " * (noLevel - i), figure * (noLevel + i), " " * (noLevel - i)
    print(levelCont)
