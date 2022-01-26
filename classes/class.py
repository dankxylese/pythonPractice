# OOP

class Dog:
    def __init__(self, name, breed, animal_kind = "canine"):  # method to initialise class variables
        self.name = name
        self.animal_kind = animal_kind  # class variable
        self.breed = breed

    def bark(self):  # method
        return "Woof! I am a " + self.animal_kind

    def loud_bark(self):
        return self.bark().upper()


class Fish:
    def __init__(self, name):
        self.name = name
        self.animal_kind = "Goldfish"  # class variable
        self.weight = 5  # kg
        self.length = 15  # cm

    def make_sound(self):  # method
        return "... \n[DIRECTOR] This is a " + self.animal_kind + \
               ". It does not make sounds."


fido = Dog("Fido", "Dalmatian")

ricardo = Fish("Ricardo")
hombrero = Fish("Hombrero")
hombrero.animal_kind = "Cod"
mariano = Fish("Mariano")
mariano.animal_kind = "Carp"

print(f"{ricardo.name} is a Fish, that is {ricardo.weight}kg and {ricardo.length}cm long. "
      f"He is a {ricardo.animal_kind}. \n{ricardo.name} can say: {ricardo.make_sound()}")


