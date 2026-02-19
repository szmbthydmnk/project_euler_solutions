# Project Euler — Problem 54
# Count how many hands player 1 wins in the provided poker hands file.
# Save the Project Euler file as 'p054_poker.txt' in the same directory (or change FILENAME below).

from collections import Counter

FILENAME = "/Volumes/THYMac/Users/ThyDominik/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0054_poker.txt"  # change to 'poker.txt' if your file has that name

VALUE_MAP = {r: i for i, r in enumerate(list('23456789TJQKA'), start=2)}

# Hand ranks (higher is better):
# 9: Straight flush
# 8: Four of a kind
# 7: Full house
# 6: Flush
# 5: Straight
# 4: Three of a kind
# 3: Two pair
# 2: One pair
# 1: High card


def is_straight(ranks):
    """Return (True, high_card) if ranks form a straight, including A-2-3-4-5 wheel."""
    rs = sorted(set(ranks))
    if len(rs) != 5:
        return False, None
    # Normal straight
    if max(rs) - min(rs) == 4:
        return True, max(rs)
    # Wheel: A-2-3-4-5 -> ranks [2,3,4,5,14]
    if rs == [2, 3, 4, 5, 14]:
        return True, 5
    return False, None


def hand_value(hand):
    """Evaluate a 5-card hand and return a tuple that compares lexicographically.
    Higher tuple means a stronger hand.
    """
    # hand: list of strings like ['5H', '5C', '6S', '7S', 'KD']
    ranks = [VALUE_MAP[c[0]] for c in hand]
    suits = [c[1] for c in hand]
    counts = Counter(ranks)
    counts_by_freq = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
    # example counts_by_freq: [(rank_with_most_count, freq), ...]

    flush = len(set(suits)) == 1
    straight, high_straight = is_straight(ranks)

    if straight and flush:
        return (9, high_straight)
    # Four of a kind
    if counts_by_freq[0][1] == 4:
        four_rank = counts_by_freq[0][0]
        kicker = counts_by_freq[1][0]
        return (8, four_rank, kicker)
    # Full house
    if counts_by_freq[0][1] == 3 and counts_by_freq[1][1] == 2:
        three_rank = counts_by_freq[0][0]
        pair_rank = counts_by_freq[1][0]
        return (7, three_rank, pair_rank)
    if flush:
        # tie-break by ranks descending
        return (6, ) + tuple(sorted(ranks, reverse=True))
    if straight:
        return (5, high_straight)
    if counts_by_freq[0][1] == 3:
        three_rank = counts_by_freq[0][0]
        kickers = [r for r in sorted(ranks, reverse=True) if r != three_rank]
        return (4, three_rank) + tuple(kickers)
    if counts_by_freq[0][1] == 2 and counts_by_freq[1][1] == 2:
        # two pair
        high_pair = counts_by_freq[0][0]
        low_pair = counts_by_freq[1][0]
        kicker = counts_by_freq[2][0]
        return (3, high_pair, low_pair, kicker)
    if counts_by_freq[0][1] == 2:
        pair_rank = counts_by_freq[0][0]
        kickers = [r for r in sorted(ranks, reverse=True) if r != pair_rank]
        return (2, pair_rank) + tuple(kickers)
    # High card
    return (1, ) + tuple(sorted(ranks, reverse=True))


def parse_line(line):
    parts = line.strip().split()
    if len(parts) != 10:
        raise ValueError("Line does not contain 10 cards: " + line)
    return parts[:5], parts[5:]


def count_player1_wins(filename=FILENAME):
    p1_wins = 0
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p1, p2 = parse_line(line)
            v1 = hand_value(p1)
            v2 = hand_value(p2)
            if v1 > v2:
                p1_wins += 1
            total += 1
    return p1_wins, total


if __name__ == '__main__':
    wins, total = count_player1_wins()
    print(f"Player 1 wins: {wins} / {total}")
    # For Project Euler problem 54 the expected answer is 376
