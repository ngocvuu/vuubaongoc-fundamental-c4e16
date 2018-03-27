height = int(input("Your height in cm?"))
weight = int(input("Your weight in kg?"))
h2 = height / 100
BMI = weight / (h2**2)
print(BMI)

if BMI < 16:
    print("Severely underweight")
elif BMI > 16 and BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
elif BMI > 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")
