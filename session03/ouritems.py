items = ["T-shirt", " Sweater"]
running = True
while running:
  want = input("Welcome to our shop, what do you want(C, R, U, D)? ")
  if want == "R":
    print("Our items: ", *items, sep = ", ")
  elif want == "C":
    new = input("Enter new item: ")
    items.append(new)
    print("Our items: ", *items, sep = ", ")
  elif want == "U":
    update = int(input("Update position: "))
    newitem = input("New item: ")
    items[update - 1] = newitem
    print("Our items: ", *items, sep = ", ")
  elif want == "D":
    delete_position = int(input("Delete position: "))
    del items[delete_position]
    print("Our items: ", *items, sep = ", ")
  else:
    running = False
