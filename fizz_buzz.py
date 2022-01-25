# FizzBuzz
# FizzBuzz game with changeable Fizz, Buzz, Range,
# and even an ability to add a third word with its own divisor

rLow = 1
rHigh = 100
fizz = "fizz"
buzz = "buzz"
addNew = False
newWord = ""
newDivisor = 0

# Processing of Input
while True:
    i0 = input("Run basic version or customisable? (basic or custom): ").lower()  # i0 = input 0
    if i0 == "custom":
        while True:
            i1 = input("Specify starting range (leave blank for 1): ")
            if i1.isdigit() and int(i1) > 0:  # check for it to be a digit (which removes float) and more than 0.
                rLow = int(i1)  # Save
                break
            elif not i1:  # If left black, use default value
                break
            else:
                print("Invalid input, try again..")

        while True:
            i2 = input("Specify ending range (leave blank for 100): ")
            if i2.isdigit() and int(i2) > 0:
                rHigh = int(i2)
                break
            elif not i2:
                break
            else:
                print("Invalid input, try again..")

        while True:
            i3 = input("Specify word instead of fizz (leave blank for fizz): ").lower()
            if i3.isalpha():
                fizz = i3
                break
            elif not i3:
                break
            else:
                print("Invalid input, try again..")

        while True:
            i4 = input("Specify word instead of buzz (leave blank for buzz): ").lower()
            if i4.isalpha():
                buzz = i4
                break
            elif not i4:
                break
            else:
                print("Invalid input, try again..")

        while True:
            i5 = input("Would you like to add a third word? (yes / no): ").lower()
            if i5 == "yes":
                while True:
                    addNew = True  # Remember if we need to process the new word
                    i6 = input("Specify the new word:").lower()
                    if i6.isalpha():
                        newWord = i6  # Save the new word
                        break
                    else:
                        print("Invalid input, try again..")
                while True:
                    i7 = input("Specify new divisor to replace dividend with word "
                               + i6 + " (has to be more than 1): ")
                    if i7.isdigit() and int(i7) > 1:
                        newDivisor = int(i7)  # Save the new divisor
                        break
                    else:
                        print("Invalid input, try again..")
                break
            elif i5 == "no":
                print("No new word today.. :(")
                break
            else:
                print("Invalid input, try again..")
        break  # Exit main loop, and go to game

    elif i0 == "basic":
        break
    else:
        print("Invalid input, try again..")

# Game
for num in range(rLow, rHigh + 1):
    if num % 3 == 0 and num % 5 == 0:  # fizz and buzz
        if addNew and num % newDivisor == 0:  # fizz, buzz and new word
            print("(" + str(num) + ")" + fizz + buzz + newWord)
            continue  # skip to the end of the for loop
        print("(" + str(num) + ")" + fizz + buzz)
    elif num % 3 == 0:  # fizz
        if addNew and num % newDivisor == 0:  # fizz and new word
            print("(" + str(num) + ")" + fizz + newWord)
            continue
        print("(" + str(num) + ")" + fizz)
    elif num % 5 == 0:  # buzz
        if addNew and num % newDivisor == 0:  # buzz and new word
            print("(" + str(num) + ")" + buzz + newWord)
            continue
        print("(" + str(num) + ")" + buzz)
    elif addNew and num % newDivisor == 0:  # new word
        print("(" + str(num) + ")" + newWord)
    else:  # normal number
        print("(" + str(num) + ")" + str(num))
