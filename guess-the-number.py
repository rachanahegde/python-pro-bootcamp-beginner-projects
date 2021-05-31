import random

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

#Number Guessing Game Objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
