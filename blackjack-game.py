############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random
from replit import clear

def deal_card():
  """ Returns a random card from the deck. """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  """ Take a list of cards and return the score calculated from the cards. """
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def check_score(user_cards, computer_cards):
  print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
  print(f"Computer's first card: {computer_cards[0]} ")
  if calculate_score(computer_cards) == 0:
    compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))
  elif calculate_score(user_cards) == 0:
    compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))
  elif calculate_score(user_cards) > 21:
    compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))

def compare(user_cards, computer_cards, user_score, computer_score):
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  if computer_score == 0:
    print("You lose!")
  elif user_score == 0:
    print("You win!")
  elif user_score > 21:
    print("You went over. You lose 😭")
  elif user_score == computer_score:
    print("It's a draw.")
  elif computer_score > 21:
    print("You win!")
  elif user_score > computer_score:
    print("You win!")
  else:
    print("You lose.") 

def computer_play(computer_cards):
  while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())

def blackjack_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game_continues = True
  
  for num in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  check_score(user_cards, computer_cards)
  computer_play(computer_cards)

  while game_continues:
    draw_card = input("Type 'y' to get another card, type 'n' to pass: ") 
    if draw_card == 'y':
      user_cards.append(deal_card())
      # check_score(user_cards, computer_cards)
      print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]} ")
      if calculate_score(computer_cards) == 0:
        compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))
        game_continues = False
      elif calculate_score(user_cards) == 0:
        compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))
        game_continues = False
      elif calculate_score(user_cards) > 21:
        compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))
        game_continues = False
    else:
      compare(user_cards, computer_cards, calculate_score(user_cards), calculate_score(computer_cards))
      game_continues = False

  user_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if user_answer == 'y':
    clear()
    blackjack_game()
  else:
    return
  
user_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if user_answer == 'y':
  clear()
  blackjack_game()
