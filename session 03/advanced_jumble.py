from random import *

word_list = ["anonymous", "champion", "adventure", "wanderlust", "necklace"]


for i in range(1, len(word_list) + 1):
  while True:
    text = choice(word_list)
    words = list(text)
    shuffle(words)
    print("Here is the hint: ", *words, sep = " ")

    guess = str(input("Enter your guess: "))

    if guess == text:
      break

  print("BINGO")
print("You're the champion!!!")

####
Lỗi: dư 1 hàng
