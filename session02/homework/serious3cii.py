n = int(input("Enter a number: "))

for i in range(1,n+1):
    print(*range(i,(n+1)*i,i))
