howmany = int(input("How many B bacterias are there? "))
howmuch = int(input("How much time in mins will we wait? "))
#check lại công thức
final = howmany * 2 ** (howmuch - 1)
sum = howmany * (1 - 2 ** howmuch) / (1 - 2)
print("After",howmuch, "minutes, we would have",sum,"bacterias")
