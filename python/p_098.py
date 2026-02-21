# Project Euler - 98 - Anagramic Squares
# Solution by Dominik Szombathy 
# Date - 2026.02.21


# Solution: 18769

from collections import defaultdict
import math


def load_words(filename):
    with open(filename, "r") as f:
        content = f.read()
    return [word.strip('"') for word in content.split(',')]


def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return [group for group in groups.values() if len(group) > 1]


def generate_squares_by_length(max_len):
    squares_by_len = defaultdict(list)
    n = 1
    while True:
        square = n * n
        length = len(str(square))
        if length > max_len:
            break
        squares_by_len[length].append(square)
        n += 1
    return squares_by_len


def is_valid_mapping(word, square):
    s = str(square)
    if len(word) != len(s):
        return None

    mapping = {}
    used_digits = {}

    for ch, digit in zip(word, s):
        if ch in mapping:
            if mapping[ch] != digit:
                return None
        else:
            if digit in used_digits:
                return None
            mapping[ch] = digit
            used_digits[digit] = ch

    if mapping[word[0]] == '0':
        return None

    return mapping


def apply_mapping(word, mapping):
    return int(''.join(mapping[ch] for ch in word))


def solve(filename="Data/0098_words.txt"):
    words = load_words(filename)
    anagram_groups = group_anagrams(words)

    max_word_len = max(len(word) for word in words)
    squares_by_len = generate_squares_by_length(max_word_len)

    max_square = 0

    for group in anagram_groups:
        length = len(group[0])
        candidate_squares = squares_by_len[length]
        square_set = set(candidate_squares)

        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                w1, w2 = group[i], group[j]
                for square in candidate_squares:
                    mapping = is_valid_mapping(w1, square)
                    if mapping:
                        mapped = apply_mapping(w2, mapping)
                        if mapped in square_set and len(str(mapped)) == length:
                            max_square = max(max_square, square, mapped)

    return max_square


if __name__ == "__main__":
    print(solve())

