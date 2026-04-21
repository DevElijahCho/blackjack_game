
import random

def draw_first_two_cards(temp_list_cards):

  temp_computerCards = random.sample(temp_list_cards, 2)
  temp_user_cards = random.sample(temp_list_cards, 2)
  return temp_computerCards, temp_user_cards
  
def draw_a_card(temp_player, cardsList):
  card_drawn = random.choice(cardsList)
  temp_player.append(card_drawn)
  
  return temp_player
  
def get_result(temp_user_cards, temp_computer_cards):
  if temp_computer_cards == temp_user_cards:
    print("======ITS A DRAW======")
  elif  temp_user_cards == 0:
    print("======BLACKJACK 21, YOU WIN!======")
  elif temp_computer_cards == 0:
    print("======DEALER GOT BLACKJACK, YOU LOSE!======")
  elif temp_user_cards > 21:
    print('======ITS A BUST YOU LOST!======')
  elif temp_computer_cards > 21:
    print("======DEALER HAND IS A BUST, YOU WIN!======")
  elif temp_computer_cards > temp_user_cards:
    print("======DEALER HAND WINS!======")
  else:
    print("======BIGGER HAND, YOU WIN!======")
    
def calculate_score(cards_list):
  if sum(cards_list) == 21 and len(cards_list) == 2:
    return 0 
    
  if sum(cards_list) > 21 and 11 in cards_list:
    cards_list.remove(11)
    cards_list.append(1)
    
  return sum(cards_list)

def main():
  CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  runGame = True

  user_play = input("Type 'y' if you want to play and 'n' if no: ").lower()
  if user_play == "y":
    print("BLACKJACK GAME")
  elif user_play == "n":
    runGame = False
      
  while runGame:
    computer_cards, user_cards = draw_first_two_cards(CARDS)
    computer_first_card = computer_cards[0]
    total_hand = calculate_score(user_cards)
    total_computer_hand = calculate_score(computer_cards)
    print(f"Dealer's First hand: {computer_first_card}\nYour hand: {user_cards} total hand: {total_hand}")
    while True:
      if total_hand == 0 or total_computer_hand == 0:
        get_result(total_hand, total_computer_hand)
        break
      user_hit_or_stand = input('Type "y" to HIT or Type "n" to STAND: ')
      if user_hit_or_stand == 'y':
        draw_a_card(user_cards, CARDS)
        total_hand = calculate_score(user_cards)
        print(f"Dealer's hand: {computer_first_card}\nYour hand: {user_cards} total: {total_hand}")
        if total_hand > 21:
          get_result(total_hand, total_computer_hand)
          break
      elif user_hit_or_stand == "n":
        while total_computer_hand < 17:
            draw_a_card(computer_cards, CARDS)
            total_computer_hand = calculate_score(computer_cards)
        get_result(total_hand, total_computer_hand)
        print(f"Dealer's hand: {computer_cards} total hand: {total_computer_hand}\nYour hand: {user_cards} total hand: {total_hand}")
        break
    user_play_again = input("Do you want to play again? Type 'y' for yes and 'n for 'no': y")
    if user_play_again == 'n':
      break
    else:
      print()
      
if __name__ == "__main__":
  main()