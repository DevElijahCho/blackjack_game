
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
runGame = True

user_play = input("Type 'y' if you want to play and 'n' if no: ")
if user_play == "y":
  print("BLACKJACK GAME")
elif user_play == "n":
  runGame = False


def draw_first_two_cards(temp_list_cards):

  temp_computerCards = random.choices(temp_list_cards, weights = [4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4], k = 2)
  temp_user_cards = random.choices(temp_list_cards, weights = [4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4], k = 2)
  
  return temp_computerCards, temp_user_cards
  
def draw_a_card(temp_player, cardsList):
  card_drawn_list = random.choices(cardsList, weights = [4, 4, 4, 4, 4, 4, 4 ,4, 4, 4, 4, 4, 4], k = 1)
  card_drawn = int(card_drawn_list[0])
  temp_player.append(card_drawn)
  
  return temp_player
  
def get_result(temp_user_cards, temp_computer_cards):
  if temp_user_cards > 21:
    print('ITS A BUST YOU LOST!')
  elif temp_computer_cards > 21:
    print("HAND IS A BUST, YOU WIN!")
  elif temp_computer_cards > temp_user_cards:
    print("DEALER HAND WINS!")
  elif temp_computer_cards == temp_user_cards:
    print("ITS A DRAW")
  else:
    print("BIGGER HAND, YOU WIN!")
    
while runGame:
  computer_cards, user_cards = draw_first_two_cards(cards)
  computer_first_card = computer_cards[0]
  total_hand = sum(user_cards)
  total_computer_hand = sum(computer_cards)
  print(f"Dealer's First hand: {computer_first_card}\nYour hand: {user_cards} total hand: {total_hand}")
  while True:
    user_hit_or_stand = input('Type "y" to HIT or Type "n" to STAND: ')
    if user_hit_or_stand == 'y':
      draw_a_card(user_cards, cards)
      total_hand = sum(user_cards)
      print(f"Dealer's hand: {computer_first_card}\nYour hand: {user_cards} total: {total_hand}")
      if total_hand > 21:
        get_result(total_hand, total_computer_hand)
        break
    elif user_hit_or_stand == "n":
      while total_computer_hand < 17:
          draw_a_card(computer_cards, cards)
          total_computer_hand = sum(computer_cards)
      get_result(total_hand, total_computer_hand)
      print(f"Dealer's hand: {computer_cards} total hand: {total_computer_hand}\nYour hand: {user_cards} total hand: {total_hand}")
      break
  user_play_again = input("Do you want to play again? Type 'y' for yes and 'n for no'")
  if user_play_again == 'n':
    break
  else:
    print()