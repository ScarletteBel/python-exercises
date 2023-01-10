# To know if I take my umbrella with me or not...

weather = input("¿Is it raining? ")


if weather.lower() == "no":
    print("Enjoy your day!")
else:
    question2 = input("¿It's very windy? ")
    if question2.lower() == "yes":
        print("it's too windy to go out with an umbrella")
    else:
        print("take an umbrella with you")


    

