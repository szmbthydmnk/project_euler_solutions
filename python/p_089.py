# Roman Numerals - 2025.10.21 - Dominik Szombathy

FilePath = '/Volumes/THYMac/Users/dominikszombathy/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0089_roman.txt'

File = open(FilePath, 'r')
Lines = File.readlines()
RomanNumerals = [line.strip() for line in Lines]
File.close()

for _ in range(len(RomanNumerals)):
    print(RomanNumerals[_])


RomanToIntMap = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def Roman_to_Integer(roman: str) -> int:
    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = RomanToIntMap[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

def Integer_to_Roman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ""
    for i in range(len(values)):
        while num >= values[i]:
            roman_numeral = roman_numeral + symbols[i]
            num -= values[i]
    return roman_numeral

Characters = 0
Original_characters = 0 

for number in range(len(RomanNumerals)):
    Original_characters += len(RomanNumerals[number])
    integer_value = Roman_to_Integer(RomanNumerals[number])
    minimal_roman = Integer_to_Roman(integer_value)
    Characters += len(minimal_roman)

print(Original_characters - Characters)
