from replit import clear
#You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")

program_running = True
silent_auction_dict = {}
def winning_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for person in bidding_record:
    if bidding_record[person] > highest_bid:
      highest_bid = bidding_record[person]
      winner = person
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while program_running:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  silent_auction_dict[name] = bid
  ask_user = input("Are there are any other bidders? Type 'yes' or 'no'. \n")
  if ask_user == 'yes':
    clear()
  else:
    winning_bid(silent_auction_dict)
    program_running = False
