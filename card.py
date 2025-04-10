import random

#card draw function here
def card_draw():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    jokers = ['Joker','Joker']

    # Decide whether to draw a joker or a regular card
    if random.random() < 0.1:  # 10% chance of drawing a joker
        return random.choice(jokers)
    else:
        return f"{random.choice(ranks)} of {random.choice(suits)}"

