#########################################
# caleb forestal
# assignment 3
# april 7 2025
#
# this makes uno cards and draws a few random ones
# input: how many cards to draw
# output: the cards drawn
#########################################

import random

# makes the full uno deck
def make_deck():
    deck = []
    colors = ['red', 'blue', 'green', 'yellow']
    nums = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    for c in colors:
        for n in nums:
            deck.append(f'{c} {n}')
        deck.append(f'{c} skip')
        deck.append(f'{c} skip')
        deck.append(f'{c} reverse')
        deck.append(f'{c} reverse')
        deck.append(f'{c} draw two')
        deck.append(f'{c} draw two')
    for _ in range(4):
        deck.append('black wild')
        deck.append('black draw four')
    return deck

# picks cards
def pick_random_cards(n):
    d = make_deck()
    drawn = []
    i = 0
    while i < n:
        x = random.choice(d)
        drawn.append(x)
        d.remove(x)
        i += 1
    return drawn

# prompt n
n = int(input('how many cards do you want [1-108]? '))

# check if n is ok
if n < 1 or n > 108:
    print('nah bro that number is not it')
else:
    cards = pick_random_cards(n)
    print('cards drawn:', ', '.join([c.title() for c in cards]))