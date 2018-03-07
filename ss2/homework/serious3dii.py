n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n-1):
        print("1", "0",end =" ")
    print("1","0")
    for j in range(n-1):
        print("0","1",end = " ")
    print("0","1")
# c da thu tach 0 va 1 ra nhung khong duoc, chi print ra duoc 1 cap 1 0 thoi.
# sai o dau r nhi?
