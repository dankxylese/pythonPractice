class Mammal:
    def __init__(self, name):
        self.warm_blooded = True
        self.name = name

    def reproduce(self):
        print("Giving birth to live young")


class Horse(Mammal):
    def __init__(self, name):
        super().__init__(name)  # add call to super init to have parent's attributes
        self.legs = 4

    pass


m = Mammal("Davis")
h = Horse("Horsey")
print(h.warm_blooded)
# m.reproduce()
