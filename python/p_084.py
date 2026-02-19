# Monopoly odds
# Problem 84


import random

N = 40  # number of squares on the board
CH = [7, 22, 36]  # Chance
CC = [2, 17, 33]  # Community Chest
G2J = 30          # Go to Jail square
JAIL = 10         # Jail position

# Chance cards (shuffled deck)
chance_cards = [
    lambda pos: 0,      # GO
    lambda pos: 10,     # JAIL
    lambda pos: 11,     # C1
    lambda pos: 24,     # E3
    lambda pos: 39,     # H2
    lambda pos: 5,      # R1
    lambda pos: next_r(pos),
    lambda pos: next_r(pos),
    lambda pos: next_u(pos),
    lambda pos: pos - 3,
] + [lambda pos: pos]*6  # remaining cards do nothing

# Community Chest cards
community_cards = [
    lambda pos: 0,   # GO
    lambda pos: 10,  # JAIL
] + [lambda pos: pos]*14

# Shuffle decks
random.shuffle(chance_cards)
random.shuffle(community_cards)

chance_index = 0
cc_index = 0

def next_r(pos):
    """Next railroad"""
    if pos < 5 or pos >= 35: return 5
    if pos < 15: return 15
    if pos < 25: return 25
    return 35

def next_u(pos):
    """Next utility"""
    if pos < 12 or pos >= 28: return 12
    return 28

def draw(deck, index):
    """Draw next card (returns function and next index)"""
    card = deck[index]
    index = (index + 1) % len(deck)
    return card, index

def roll_dice():
    """Roll two 4-sided dice"""
    return random.randint(1, 4), random.randint(1, 4)

# Simulation
visits = [0] * N
pos = 0
doubles = 0

for _ in range(10_000_000):
    d1, d2 = roll_dice()
    if d1 == d2:
        doubles += 1
    else:
        doubles = 0

    if doubles == 3:
        pos = JAIL
        doubles = 0
    else:
        pos = (pos + d1 + d2) % N

        # Go to Jail
        if pos == G2J:
            pos = JAIL

        # Community Chest
        elif pos in CC:
            card, cc_index = draw(community_cards, cc_index)
            pos = card(pos)

        # Chance
        elif pos in CH:
            card, chance_index = draw(chance_cards, chance_index)
            pos = card(pos)
            # If card moved to CC or G2J, process again
            if pos == G2J:
                pos = JAIL
            elif pos in CC:
                card, cc_index = draw(community_cards, cc_index)
                pos = card(pos)

    visits[pos] += 1

# Get top 3
top3 = sorted(range(N), key=lambda i: visits[i], reverse=True)[:3]
print("Top 3 squares:", top3)
print("Answer:", "".join(f"{x:02d}" for x in top3))