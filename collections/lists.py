shopping_list = ["eggs", "bread", "bananas", "tea"]
mixed = [[1, 2, 3], 1, 2, 3, 4, True, "test"]

shopping_list.pop(2)
print(shopping_list)
shopping_list.append("bisquits")
shopping_list.insert(0, "apples")
#shopping_list.remove("bananas")
print(shopping_list)

a = mixed[0]

print(a[0])

# Tuples

colours = ("red", "blue", "green")

# Tuples are IMMUTABLE - can't be changed


table = {
  "brand": "Ford",
  "year": 1964,
  "models": {
      "1": "Fiesta",
      "2": "Hombrero",
    }
}


x = table.get("brand") # allows optional return in key not found
y = table["brand"]

print(table.get("models").get("1"))

