# This is what we will use for the video intro to dictionaries.

# Type in the things that you've learned:

# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates.

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))

#if capitals.get("Russia"):
#    print("That capital exists in this dictionary!")
#else:
#    print("That capital doesn't exist in this dictionary!")

# How to update keys

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#print(capitals)

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")