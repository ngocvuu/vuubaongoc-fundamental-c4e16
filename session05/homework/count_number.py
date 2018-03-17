numbers = [1, 6, 8, 1, 2, 1, 5, 6]
ask = int(input("Enter a number to know its occurrence: "))

#ko dùng hàm count thì làm sao mà tìm
count = 0
for i in numbers:
    if i == ask:
        count += 1
print(ask, "appears", count, "times in my list")
