print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def find_divisors(num):
    temp_list = []
    for i in range(1, num):
        if num % i == 0:
            temp_list.append(i)
    return temp_list


print(find_divisors(12))

print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factor_finder(num, num1):
    if num1 in find_divisors(num):
        return True
    elif num in find_divisors(num1):
        return True
    else:
        return False


print(factor_finder(27, 3))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", " "]


# A2a:
def alpha_pos_finder(letter: str):
    return alphabet.index(letter)


print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def alpha_name_pos_finder(name: str):
    temp_string = ""
    for letter in name:
        temp_string += str(alpha_pos_finder(letter.lower()))

    return temp_string


print(alpha_name_pos_finder("Vlad"))

print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def pass_from_anpf(name: str):
    user_id = alpha_name_pos_finder(name)
    total = 0
    for number in user_id:
        total += int(number)
    return int(user_id) - total


print(pass_from_anpf("Bob"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime_finder_helper(number: int):
    flag_not_prime = False
    for i in range(2, number):
        if number % i == 0 or number == i:
            flag_not_prime = True

    if flag_not_prime:
        return False
    else:
        return True


print("\nQ3b\n")


# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def prime_finder(user_input):  # can be int or str
    if str(user_input).isdigit():
        if prime_finder_helper(int(user_input)):
            return True
        else:
            return False
    else:
        return "Invalid Input"


print(prime_finder("thing"))
print(prime_finder(102))
print(prime_finder(121))
print(prime_finder(102))
print(prime_finder(103))
print(prime_finder("103"))

# -------------------------------------------------------------------------------------- #
