# Improving with the while basics...

total = 3

plusNum = int(input("Insert the adding number: "))

i = total 
while i < 50:
    i += plusNum
    print(i)

#Another one...

num = int(input("Insert a number: "))

i = num
while i < 42:
        break
    print(i)
    print(int(input("The number must larger than 42, try again: ")))
    print("Number inserted succesfully!")
    
    
  

# Email = True
# while Email:
#     print("Execute Me")
#     Email = False # Break the while loop here
#     if not Email:
#         break
#     print("Never execute me")