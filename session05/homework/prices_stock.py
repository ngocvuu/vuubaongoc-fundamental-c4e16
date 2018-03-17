prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3

}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15

}

# for fruit in prices:
#     print(".",fruit,":", prices[fruit],sep = " ")
# print()

what = input("which fruit do you want? ")
print(".",what)
if what in prices:
    print(". price : ",prices[what])
if what in stock:
    print(". stock : ",stock[what])

total = 0

for fruit in prices:
    total = total + (prices[fruit] * stock[fruit])
print("The total price: ",total)
