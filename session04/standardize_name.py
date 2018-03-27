
name = input("Your full name: ")

n = name.lower().title()

print("Your second name: ",n)

real_name = n.replace("  ", "")

print("Your final name: ",real_name)
# Số chẵn space thì ok nhưng số lẻ space thì chập luôn :v
