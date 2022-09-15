import random
tries = 0
num = random.randint(1,11)

while tries < 3:
  print("Guess a number 1 - 10 ")
  guess = int(input())
  tries = tries + 1
  if guess < num:
    print("Too Low!")

  if guess > num:
    print("Too High!")

  if guess == num:
    print("Correct!")
    break
  if tries == 3 and guess != num:
    print("You failed to guess the number!")