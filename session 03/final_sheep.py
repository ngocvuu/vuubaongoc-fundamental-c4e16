flock_size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Ngoc and these are my sheep sizes: ", flock_size)
m = max(flock_size)
print("Now my biggest sheep has size ", m, "Let's shear it")

for x, i in enumerate(flock_size):
    if i == m:
      flock_size[x] = 8

print("After shearing, here is my flock",flock_size)

month = int(input("Enter no months: "))
for mon in range(1,month+1):

  flock_size = [x + 50 for x in flock_size]
  print("MONTH",mon,":")
  print("One month has passed, now here is my flock", flock_size)

  m = max(flock_size)
  print("Now my biggest sheep has size ", m, "Let's shear it")

  if mon == month:
    break

  for x, i in enumerate(flock_size):
    if i == m:
      flock_size[x] = 8

  print("After shearing, here is my flock",flock_size)

total = sum(flock_size)

print("My flock has size in total: ", total)
print("I would get", total * 2, "$")
