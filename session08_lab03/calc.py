x = int(input("x = "))
operation = input("Operation(+,-,*,/): ")
y = int(input("y = "))

result = 0

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
else:
    result = x / y

print("*" * 20)
print("{0} {1} {2} = {3}".format(x,operation,y,result))
print("*" * 20)
