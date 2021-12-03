"""
Assignment 10.1
Cassidy Hall
This code shows a class, and
"""

# This is the created class with three
class shelter:
    def __init__(self, species, breed):
        self._species = species
        self._breed = breed
    # These are the methods used for getting the species and breeds, as well as being able to change the species and breeds
    def get_species(self):
        return self._species
    def get_breed(self):
        return self._breed
    def set_species(self, species):
        self._species = species
        pass
    def set_breed(self, breed):
        self._breed
        pass

# These are the objects within the class
a1 = shelter("Dog", "Shiba Inu")
a2 = shelter("Dog", "Pug")
a3 = shelter("Cat", "Russian Blue")
a4 = shelter("Cat", "Maine Coon")

# This is one of two functions that changes the value
def take_home():
    add = input("Would you like to take a pet home?\nYes/No\n")
    if add == "Yes":
        take = input("Which would you like to take home?\n1) Shiba Inu\n2) Pug\n3) Russian Blue\n4) Maine Coon\n5) Nevermind\n")
        if take == "1":
            a1.set_species("Taken home!")
            a1.set_breed("Taken home!")
        elif take == "2":
            a2.set_species("Taken home!")
            a2.set_breed("Taken home!")
        elif take == "3":
            a3.set_species("Taken home!")
            a3.set_breed("Taken home!")
        elif take == "4":
            a4.set_species("Taken home!")
            a4.set_breed("Taken home!")
        elif take == "5":
            print("Please take your time!")
        else:
            print("Please pick a number from the list")
            take_home()

# This is the other function that shows all the values of the classes
def see_animals():
    see = input("Please enter a number to the corresponding answer\n1) Dogs\n2) Cats\n3) Both\n")
    if see == "1":
        print("Here are the breeds we have available:")
        print(a1._breed)
        print(a2._breed)
    elif see == "2":
        print("Here are all the breeds we have available:")
        print(a3._breed)
        print(a4._breed)
    elif see == "3":
        print("Here are all the breeds available:")
        print("Dogs:")
        print(a1._breed)
        print(a2._breed)
        print("Cats:")
        print(a3._breed)
        print(a4._breed)
    else:
        print("Please enter a number")
        see_animals()

# The main function, which is also where the demo program takes place
def main():
    print("Welcome to the shelter! Which animals would you like to see?")
    see_animals()
    take_home()
    

if __name__ == "__main__":
    main()