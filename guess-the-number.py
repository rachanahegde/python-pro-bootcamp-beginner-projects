import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
#print(f"Pssst, the correct answer is {random_number}.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'easy':
  attempts = 10
else:
  attempts = 5

game_continues = True
while game_continues:
  print(f"You have {attempts} attempts remaining to guess the number.")
  user_guess = int(input("Make a guess: "))
  attempts -= 1
  if user_guess > random_number:
    print("Too high.")
  elif user_guess < random_number:
    print("Too low.")
  else:
    print(f"You got it! The answer was {random_number}.")
    game_continues = False

  if attempts != 0:
    print("Guess again.")
  elif attempts == 0 and user_guess != random_number:
    print("You've run out of guesses, you lose.")
    game_continues = False
