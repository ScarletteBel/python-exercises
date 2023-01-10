
# your_num = int(input("Enter a number:"))
# while (your_num > 0):
#     product = your_num * 5
#     print(your_num, " * 5 = ", product)
#     your_num -= 1


# sum = 0
# for i in range(0, 25, 5):
#     sum += i
# print(sum)



# countries = {"CA": "Canada",
#              "US": "United States",
#              "GB": "Great Britain",
#              "MX": "Mexico"}
# code = "IE"
# country = countries.pop(code, "Unknown country")
# print(country + " was deleted.")

# from tkinter import Y


# num_widgets = 0
# while True:
#     choice = input("Would you like to buy a widget? (y/n): ")
#     if choice.lower() == "y":
#         num_widgets += 1
#     else:
#         break
# print("You bought", num_widgets , "widget(s).")


# pets = {
#     "dog": {"type": "poodle", "color": "white"},
#     "cat": {"type": "Siamese", "color":  "black and white"},
#     "bird": {"type": "parrot", "color": "green"}
# }
# pet = pets["dog"]
# pet = pets["bird"]
# print(pet["color"], pet["type"])

def get_username(first, last):
    s = first + "." + last
    return s.lower()

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = get_username(first_name, last_name)
    print("Your username is: " + username)
    
if __name__ == "__main__":
    main()