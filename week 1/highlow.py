import random
import json
import pygame

pygame.mixer.init()

correct_answer_sound = pygame.mixer.Sound("newturn.mp3")
wrong_sound = pygame.mixer.Sound("footsteps.mp3")
background_music = pygame.mixer.music.load("bgsong.mp3")

pygame.mixer.music.play(-1, 0.0)

with open(r'week 1\data.json', 'r') as file:
    data = json.load(file)[0]

def get_random_artist():
    return random.choice(list(data.keys()))

score = 0
playing = True
artist1 = get_random_artist()
listeners1 = data[artist1]

while playing:
    artist2 = get_random_artist()
    while artist2 == artist1:
        artist2 = get_random_artist()

    listeners2 = data[artist2]

    print(f"\nWho has more monthly listeners on Spotify?")
    print(f"A: {artist1} ({listeners1} listeners)")
    print(f"B: {artist2} (?? listeners)")
    guess = input("Type 'A' or 'B': ").strip().upper()


    correct_answer = 'A' if listeners1 > listeners2 else 'B'

    if guess == correct_answer:
        score += 1
        print(f"Correct! Your score: {score}")
        correct_answer_sound.play()
        artist1, listeners1 = (artist1, listeners1) if correct_answer == 'A' else (artist2, listeners2)
    else:
        print(f"Wrong! {artist1} has {listeners1}, {artist2} has {listeners2}.")
        print(f"Game over! Your final score: {score}")
        wrong_sound.play()
        pygame.mixer.music.stop()
        playing = False

pygame.time.delay(2000)