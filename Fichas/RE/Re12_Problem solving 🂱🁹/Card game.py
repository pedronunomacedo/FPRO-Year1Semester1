import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def card_value(card):
    if card[1] in ['2','3','4','5','6','7','8','9','10']:
        if card[0] not in ['♣','♠']:
            return int(card[1])
        else:
            return int(card[1]) * 2
    if card[1] in ['J','Q','K']:
        if card[0]  not in ['♣','♠']:
            return 10
        else:
            return 10 * 2    
    if card[1] == 'A':
        if card[0] not in ['♣','♠']:
            return 11
        else:
            return 11 * 2

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

f={}
winners = {'P1':0 ,'P2':0, 'P3':0, 'P4':0}

def play(s) -> None:
    random.seed(s)
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            f[name]=card_value(card)
            
            # print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        
        cards_pro = sorted(f, key = lambda x: f[x], reverse = True)
        for i in f.keys():
            if f[i] == f[cards_pro[0]]:
                winners[i] += 1
    list_final = []
    maximo = max(winners, key = lambda x: winners[x])
    
    for player in winners.keys():
        if winners[player] == winners[maximo]:
            list_final.append(player)
    final_winners = ""        
    for winner in list_final:        
        final_winners += winner + " "
    return final_winners         

print(play(123))