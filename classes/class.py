# OOP

class Dog:
    animal_kind = "canine"  # class variable

    def bark(self):  # method
        return "Woof! I am a " + self.animal_kind


class Fish:
    animal_kind = "Gold"  # class variable
    weight = 5  # kg
    length = 15  # cm

    def make_sound(self):  # method
        return "... \n[DIRECTOR] This is a " + self.animal_kind + " fish. It does not make sounds."


fido = Dog()

ricardo = Fish()
hombrero = Fish()
hombrero.animal_kind = "Cod"
mariano = Fish()
mariano.animal_kind = "Carp"

print(ricardo.animal_kind)
print(hombrero.animal_kind)
print(mariano.animal_kind)

# print(fido, type(fido))
# print(fido.animal_kind)
# print(fido.bark())
# print(ricardo.make_sound())
# print("His weight is " + str(ricardo.weight) + "kg")


