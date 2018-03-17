inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] =  ["seashell", "strange berry", "lint"]
inventory["backpack"].remove("dagger")
print(inventory, end = "\t")
print()

inventory["gold"] += 50
print(inventory, end = "\t")
print()
