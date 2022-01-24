#print("hello world")

# both are strings

#print("hello world"[1])  # strings are lists of characters. Access last char with [-1]
#print(len("hello world"))  # length of a string

#print("Bibhutibhushan Bandyopadhyay"[-29].strip())  # bounds can go over, they will be ignored

hi = "Hello World"
print(hi
      .replace(" ", "")
      .isalpha())
print(hi
      .lower()
      .islower())
print(hi
      .upper()
      .isupper())
print(hi
      .endswith("d"))
print(hi
      .startswith("H"))

