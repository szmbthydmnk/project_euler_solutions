from itertools import product

def decrypt(cipher, key):
    return [c ^ k for c, k in zip(cipher, key * (len(cipher)//len(key) + 1))]

def problem_59():
    # Load cipher text
    with open("/Volumes/THYMac/Users/ThyDominik/Programming/DomcsisEpicTinkerBox/ProjectEulerSolutions/Data/0059_cipher.txt") as f:
        cipher = list(map(int, f.read().split(',')))

    # Generate all 3-letter lowercase keys
    for key_tuple in product(range(ord('a'), ord('z')+1), repeat=3):
        key = list(key_tuple)
        decrypted = decrypt(cipher, key)
        text = ''.join(map(chr, decrypted))

        # Simple English check
        if " the " in text and "and" in text:
            print("Key:", ''.join(map(chr, key)))
            print("Message sample:", text[:200], "...")
            return sum(decrypted)

print(problem_59())