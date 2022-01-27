print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
i = 0
while i < 5:
    print(x[i])
    i += 1

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for j in x:
    if j % 2 == 0:
        print(j)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
i = 0
while i < 5:
    if x[i] % 2 == 0:
        print(x[i])
    i += 1

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
name_letters: list[str] = []
for name in names:
    name_letters.append(name[:1])
print(name_letters)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
name_spaces: list[int] = []
for name in names:
    name_spaces.append(name.index(" "))
print(name_spaces)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
fname_letters: list[str] = []
for name in names:
    spc = name.index(" ") + 1
    fname_letters.append(name[:1] + " " + name[spc:spc + 1])
print(fname_letters)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

# A3a:
for list1 in list_of_lists:
    tempSet = set()
    # for item in list1:
    #     tempSet.add(item)
    tempSet = set(list1)
    if len(list1) != len(tempSet):
        print(list1)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
while True:
    i1 = input("Input a number greater than 100: ")
    if i1.isdigit() and int(i1) > 100:  # check for it to be a digit (which removes float) and more than 0.
        break
    else:
        print("Invalid input, try again..")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
# while True:
#     i1 = input("Input a number greater than 100: ")
#     if i1.isdigit() and int(i1) > 100:
#         i1 = int(i1)
#         if (i1 % 2 != 0 and i1 != 2) \
#                 and (i1 % 3 != 0 and i1 != 3) \
#                 and (i1 % 4 != 0 and i1 != 4) \
#                 and (i1 % 5 != 0 and i1 != 5) \
#                 and (i1 % 6 != 0 and i1 != 6) \
#                 and (i1 % 7 != 0 and i1 != 7) \
#                 and (i1 % 8 != 0 and i1 != 8) \
#                 and (i1 % 9 != 0 and i1 != 9):
#             print("prime")
#         else:
#             print("not prime")
#     else:
#         print("Invalid input, try again..")

#THIS IS WRONG ^ (see functions_ex for correct)