#from replit import clear
from game_data import data
import random

game_continues = True
comparison_A = random.choice(data)
comparison_B = random.choice(data)

def compare_followers(comp_a, comp_b):
  """ Takes two random accounts, compares the follower counts, and returns the account with more followers. """
  winner = ""
  #clear()
  print("Welcome to the Higher Lower Game!")
  if score > 0:
    print(f"You're right! Current score: {score}.")
  
  print(f"Compare A: {comp_a['name']}, a {comp_a['description']}, from {comp_a['country']}.")
  print("vs")
  print(f"Against B: {comp_b['name']}, a {comp_b['description']}, from {comp_b['country']}.")

  #print(f"A has {comp_a['follower_count']} million followers") #For Debugging
  #print(f"B has {comp_b['follower_count']} million followers") #For Debugging

  #Compare Person A and Person B follower counts.
  if comp_a['follower_count'] > comp_b['follower_count']:
    winner = "A"
  else:
    winner = "B"
  return winner

#Check whether the user is correct. If the user is correct, add 1 to their score and print the score.
score = 0
def check_answer(answer, winner, score):
  """ Takes the user's answer, the account with more followers, and user's score. Checks if the user's answer is correct and returns the updated score."""
  if answer == winner:
    score += 1
  return score

while game_continues:
  winner = compare_followers(comparison_A, comparison_B)
  #Tell the user to choose who has more followers.
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  score = check_answer(answer, winner, score)
  if answer == winner:
    comparison_A = comparison_B
    comparison_B = random.choice(data)
  else:
    #clear()
    print("Welcome to the Higher Lower Game!")
    print(f"Sorry, that's wrong. Final score: {score}")
    game_continues = False

#TO DO
# Select person for comparison A and tell the user.
# Select person for comparison B and tell the user.
#Tell the user to choose who has more followers.
#Compare Person A and Person B follower counts.
#Check whether the user is correct. If the user is correct, add 1 to their score and print the score. 
## The person from comparison B becomes comparison A. Select a new person for comparison B.
#If the user is wrong, tell them and print their final score. End game.
