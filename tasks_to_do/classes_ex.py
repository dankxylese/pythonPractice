print("\nQ1a\n")


# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class Country:
    def __init__(self, name, continent, climate, language):
        self.co_name = name
        self.continent = continent
        self.climate = climate
        self.language = language

    def __str__(self):
        return f"Name: {self.co_name} \nContinent: {self.continent} \nClimate: {self.climate} \nLanguage: {self.language}"

    def get_name(self):
        return self.co_name


country = Country("Ukraine", "Europe", "Continental", "Ukrainian")
print(country)

print("\nQ1b\n")


# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
class City(Country):
    def __init__(self, name, country_name, continent, climate, language):
        super().__init__(country_name, continent, climate, language)
        self.ci_name = name  # City Name

    def __str__(self):
        return f"City Name: {self.ci_name} \nCountry: {super().get_name()} \nContinent: {self.continent} \nClimate: {self.climate} \nLanguage: {self.language}"


city = City("Kyiv", "Ukraine", "Europe", "Continental", "Ukrainian")
print(city)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


# A2a:
# for n in list_of_numbers:
#     i = Number(n)
#     if i.is_prime():
#         print(f"{n} is a prime")
#     else:
#         print(f"{n} is not a prime")

list_of_primes = list()
for n in list_of_numbers:
    if Number(n).is_prime():
        list_of_primes.append(n)
print(list_of_primes)

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
list_of_divisibles = list()

for n in list_of_numbers:
    if Number(n).divisible_by_n(3) and Number(n).divisible_by_n(4):
        list_of_divisibles.append(n)

print(list_of_divisibles)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


b = GoodBoss("Vlad", "Perfect", "Professional", "Saved")
print(b.name, b.behaviour, b.attitude, b.face)

# A3a:


# -------------------------------------------------------------------------------------- #
