
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(list_cards):
  """ Take a list of cards and return the score calculated as the sum of the list of card values"""
  score = sum(list_cards)
  if(len(list_cards) ==2 and score == 21):
    return 0
  elif (11 in list_cards and score>21):
    list_cards.remove(11)
    list_cards.append(1)
    score = sum(list_cards)
  return score



def compare(user_score,computer_score):
  if(user_score == computer_score):
    return "It's a draw :|"
  elif (computer_score==0):
    return "You lose, opponent has a BLACKJACK! :("
  elif (user_score==0):
    return "Congratulations You win with a BLACKJACK!! :)"
  elif user_score>21:
    return "BUST. You went over. You lose :("
  elif computer_score >21:
    return "Opponent went over. Congratulations !! You win!! :)"
  elif user_score > computer_score:
    return "Congratulations!! You win!! :)"
  else:
    return "You lose :("


def play_blackjack():
  print(logo)
  user_cards = [deal_card() for i in range(0,2)]
  computer_cards = [deal_card() for i in range(0,2)]
  is_game_over=False
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over=True
    else:
      user_wants_to_deal = input("Type 'h' to deal a card (HIT) or 's' to pass (STAND):\n")
      if(user_wants_to_deal == 'h'):
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  while computer_score != 0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  print(f"Your final hand is {user_cards} and final score is {user_score}")
  print(f"Computer's final hand is {computer_cards} and final score is {computer_score}")
  
  print(compare(user_score,computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n':\n") == 'y':
  os.system('clear')
  play_blackjack()


