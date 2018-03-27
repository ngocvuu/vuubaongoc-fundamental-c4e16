from random import *

text = "camping"
words = list(text)
shuffle(words)
print("Here is the hint: ", *words, sep = " ")

while True:
  guess = str(input("Enter your guess: "))

  if guess == text:
    break

  shuffle(words)
  print("Here is the hint: ", *words, sep = " ")

print("BINGO")
