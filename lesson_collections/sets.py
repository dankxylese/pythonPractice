pokemon = {"Bulbasaur", "Squirtle", "Charmander"}
# set ^

pokemon.add("Pikachu")
print(pokemon)

# unordered - can't get an items by index

pokemon.discard("Bulbasaur")
print(pokemon)

pokemon.add("Bulbasaur")
pokemon.add("Bulbasaur")
print(pokemon)
# can't have multiples of items

lst = [1, 2, 3, 1, 3, 1, 3, 2, 3, 3]
print(lst)
print(set(lst))
# can remove duplicates by casting to a set

#Frozen set

x = frozenset(["let", "it", "go"])
print(x)
# immutable^
