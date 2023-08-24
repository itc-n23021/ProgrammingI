import random

name = "nakajima'

while True:
    random_alphabet = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(random_alphabet)

    if random_alphabet.upper() == name[0].upper():
        break
