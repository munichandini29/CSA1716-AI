from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)
letters = list(letters)

for digits in permutations(range(10), len(letters)):

    mapping = dict(zip(letters, digits))

    # Leading letters cannot be zero
    if mapping["S"] == 0 or mapping["M"] == 0:
        continue

    send = (
        mapping["S"] * 1000 +
        mapping["E"] * 100 +
        mapping["N"] * 10 +
        mapping["D"]
    )

    more = (
        mapping["M"] * 1000 +
        mapping["O"] * 100 +
        mapping["R"] * 10 +
        mapping["E"]
    )

    money = (
        mapping["M"] * 10000 +
        mapping["O"] * 1000 +
        mapping["N"] * 100 +
        mapping["E"] * 10 +
        mapping["Y"]
    )

    if send + more == money:
        print("Solution found:")
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        print("\nLetter-Digit Mapping:")

        for letter in sorted(mapping):
            print(letter, "=", mapping[letter])

        break
