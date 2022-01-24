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

