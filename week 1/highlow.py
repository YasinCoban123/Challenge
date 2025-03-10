import random
import json

# Load JSON data
with open(r'week 1\data.json', 'r') as file:
    data = json.load(file)[0]  # Extract the dictionary from the list

def get_random_artist():
    return random.choice(list(data.keys()))

score = 0
playing = True

while playing:
    artist1 = get_random_artist()
    artist2 = get_random_artist()
    while artist2 == artist1:
        artist2 = get_random_artist()

    listeners1 = data[artist1]
    listeners2 = data[artist2]

    print(f"\nWho has more monthly listeners on Spotify?")
    print(f"A: {artist1} ({listeners1} listeners)")
    print(f"B: {artist2} (?? listeners)")
    guess = input("Type 'A' or 'B': ").strip().upper()

    correct_answer = 'A' if listeners1 > listeners2 else 'B'

    if guess == correct_answer:
        score += 1
        print(f"Correct! Your score: {score}")
    else:
        print(f"Wrong! {artist1} has {listeners1}, {artist2} has {listeners2}.")
        print(f"Game over! Your final score: {score}")
        playing = False
