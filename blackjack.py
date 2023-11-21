import random
playerIn = True
dealerIn = True

# Deck of cards a.k.a player cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        'Jack', 'Queen', 'King', 'Ace',
        'Jack', 'Queen', 'King', 'Ace',
        'Jack', 'Queen', 'King', 'Ace',
        'Jack', 'Queen', 'King', 'Ace'
        ]

player_cards = []
dealer_cards = []

# Dealing the cards out a.k.a dealer cards
def dealing_cards(turn):
    cards = random.choice(deck)
    turn.append(cards)
    deck.remove(cards)

# Calucate the total
def total(turn):
    total = 0
    face = ['Joker', 'Queen', 'King']
    for cards in turn:
        if cards in range(1, 11):
            total += cards
        elif cards in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

# The Result of the game
def showDealerCards():
    if len(dealer_cards) == 2:
        return dealer_cards[0]
    elif len(dealer_cards) > 2:
        return dealer_cards[0], dealer_cards[1]

# The loop
for _ in range(2):
    dealing_cards(dealer_cards)
    dealing_cards(player_cards)

print(dealer_cards)
print(player_cards)
    
while playerIn or dealerIn:
    print(f"Dealer had {showDealerCards()} and X")
    print(f"You have {player_cards} for total of {total(player_cards)}")
    if playerIn:
        stayOrhit = input("1: Stay\n2: Hit\n")
    if total(dealer_cards) > 16:
        dealerIn = False
    else:
        dealing_cards(dealer_cards)
    if stayOrhit == '1':
        playerIn = False
    else:
        dealing_cards(player_cards)
    if total(player_cards) >= 21:
        break
    elif total(dealer_cards) >= 21:
        break

# Conditions
if total(player_cards) == 21:
    print(f"You have {player_cards} for a total of {total(player_cards)} and the dealer has {dealer_cards} for a total of {total(dealer_cards)}")
    print("Blackjack! You Win")
elif total(dealer_cards) == 21:
    print(f"You have {player_cards} for a total of {total(player_cards)} and the dealer has {dealer_cards} for a total of {total(dealer_cards)}")
    print("You Lose")
elif total(player_cards) > 21:
    print(f"You have {player_cards} for a total of {total(player_cards)} and the dealer has {dealer_cards} for a total of {total(dealer_cards)}")
    print("You Bust, You Lose")
elif total(dealer_cards) > 21:
    print(f"You have {player_cards} for a total of {total(player_cards)} and the dealer has {dealer_cards} for a total of {total(dealer_cards)}")
    print("Dealer Bust, You Win")
elif 21 - total(dealer_cards) < 21 - total(player_cards):
    print(f"You have {player_cards} for a total of {total(player_cards)} and the dealer has {dealer_cards} for a total of {total(dealer_cards)}")
    print("Dealer Wins")
elif 21 - total(dealer_cards) > 21 - total(player_cards):
    print(f"You have {player_cards} for a total of {total(player_cards)} and the dealer has {dealer_cards} for a total of {total(dealer_cards)}")
    print("You Win")
    
