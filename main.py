cat_attributes = {
    "intelligence": 99,
    "energy": 78,
    "weight": 7,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats. 4. Kill your cat")

    if option == '1':
        run = input("Oh! Sorry it turns out that your cat does not like you and it may kill you!! WOULD YOU LIKE TO RUN?")
        x = run.upper()
        if x == "YES":
            print("You did not make it, you are dead lol. :)")
        else:
            print("Do you not value life?")
        pass
    elif option == '2':
        a = input("Sorry your cat is way too stubborn, would you like to try again?")
        b = a.upper()
        if b = "YES":
            print("The first lesson of today is teaching the cat how to use the litterbox")
        else:
            print("You are not even giving the cat a chance, so by force you will train the cat")
            print("The first lesson of today is teaching the cat how to use the litterbox")
        pass
    # elif ...
    else:

        pass

    # finish off the if statements below
 if cat_attributes['energy'] < 0:
        pass
    # elif ...