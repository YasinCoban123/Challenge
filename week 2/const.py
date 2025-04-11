import random
import time
from time import sleep
import pygame 

pygame.mixer.init()

intromelody = pygame.mixer.Sound("soundw2/intromelody.mp3")
bgsong = pygame.mixer.Sound("soundw2/bgsong.mp3")
newturn = pygame.mixer.Sound("soundw2/newturn.mp3")
wall_damage = pygame.mixer.Sound("soundw2/wall_damage.mp3")
win_sound = pygame.mixer.Sound("soundw2/footsteps.mp3")
lose_sound = pygame.mixer.Sound("soundw2/newturn.mp3") 


def slow_print(text, delay=0.03): 
    for char in text:
        print(char, end='', flush=True)  
        sleep(delay)
    print()  

def slower_print(text):
    slow_print(text, delay=0.03)

# Beetje lore voor de begin van het spel
lore = """
You are Emperor Constantine XI. Your empire has been in decline for a thousand years,
and now the end seems truly near. The Ottomans, having conquered most of your lands
over the past 150 years, stand ready to attempt the impossible: to take Constantinople.

Many empires have tried throughout history, but none have succeeded. The Theodosian Walls
have kept invaders out for centuries. But now, with only ten thousand men left in your realm,
the situation feels hopeless.

The Ottomans, two hundred thousand strong, are at your gates. Can you hold them off long enough
for help from the Pope? How slim that may be. Or will the last Roman successor cease to exist?
"""

# functie voor de lore
def game_intro():
    intromelody.play() # intro liedje spelen
    slower_print(lore) 
    input("\nPress ENTER to begin...")
    intromelody.stop()

# 4 keuzes van verdediging in de spel
defense_options = {
    "1": "Archers on the wall",
    "2": "Pour boiling oil",
    "3": "Repair the wall",
    "4": "Make secret ditches around the wall"
}

# de vijf vijanden die in de spel zijn, in de tuple staat de laagste en hoogste mogelijk aanval
commanders = {
    "Ibrahim Pasha": (100, 200),
    "Evrenos": (50, 100),
    "Haim Fahri": (30, 60),
    "Omer Pasha": (70, 120),
    "Sultan Mehmet II": (250, 250)
}

# beginwaardes vastzetten
wall_hp = 1000
turn = 1 
pope_response_turn = random.randint(5, 10)  # 50/50 kans dat de pope helpt tussen beurt 5 en 10

# vijf functies voor elke commandant, die de verdediging van de muur berekenen
# elke commandant heeft zijn zwakke punt, behalve de sultan
def defend_ibrahim(choice, attack):
    return calculate_damage(choice == "4", attack, "Ibrahim Pasha")

def defend_evrenos(choice, attack):
    return calculate_damage(choice == "1", attack, "Evrenos")

def defend_haim(choice, attack):
    return calculate_damage(choice == "2", attack, "Haim Fahri")

def defend_omer(choice, attack):
    return calculate_damage(choice == "3", attack, "Omer Pasha")

def defend_sultan():
    slow_print("Sultan Mehmet II cannot be defended against, he strikes furiously.")  # De sultan kan niet worden tegengehouden
    wall_damage.play()
    return 250  # returned 250 schade aan de wall

# hier berekenen hoeveel schade er gaat worden gemaakt tegen de muur
def calculate_damage(correct, attack, name):
    if correct:  # als je de correcte verdediging kiest, krijg je minder schade
        slow_print(f"You countered {name} effectively!")
        damage = int(attack * 0.5)
    else:
        slow_print(f"{name} breaks through your defenses!")  # dus als je de incorrecte verdediging kiest
        damage = attack  # hier krijg je de schade die de commandant doet
    slow_print(f"The wall takes {damage} damage.")  # laat zien hoeveel schade er is gedaan
    wall_damage.play()
    return damage  # geeft de schade terug

# functie die een random commandant pakt uit de dict
def get_commander():
    name = random.choice(list(commanders.keys()))  # pakt een random naam uit de dict
    low = commanders[name][0]  # pakt de eerte waarde uit de tuple
    high = commanders[name][1]  # pakt de tweede waarde uit de tuple
    attack = random.randint(low, high)  # gebruikt random om te kiezen tussen de twee waardes
    return name, attack # geeft de naam en de aanval terug

# main game
def constantinople():
    global wall_hp, turn  # global om de vastgestelde waardes hier te gebruiken

    game_intro()  # speelt de intro functie
    bgsong.set_volume(0.7) 
    bgsong.play(-1)  # -1 zodat die in een loop blijft spelen

    # while loop die doorgaat totdat de muur hp 0 1
    while wall_hp > 0:
        slow_print(f"\nTurn {turn}")  # laat de huidige beurt zien, /n voor een nieuwe regel
        slow_print(f"Wall HP: {wall_hp}")  #  laat de muur hp zien

        # if om te kijken of paus heeft gearegeerd
        if turn == pope_response_turn:
            if random.choice([True, False]):  # 50/50 kans dat de paus helpt
                bgsong.stop()  # stopt de achtergrond muziek
                win_sound.play()  # win geluid
                slow_print("\nThe Pope has sent reinforcements! The Ottomans retreat!")
                slow_print("The Eastern Roman Empire lives, for now...")
                time.sleep(30)  # paar secondjes wachten voor het spel beeindigt
                return  # return om de functie te beeindigen, en dus ook het spel
            else:
                slow_print("\nThe Pope has refused to send help... You're on your own.")  # Paus helpt niet, spel gaat door

        name, attack = get_commander()  # pakt de random commandant en aanval
        slow_print(f"\nOttoman commander: {name} is attacking!")  # laat zien wie er aanvalt
        slow_print("Choose your defense:")  # vraagt je om een keuze

        # verschillende opties voor verdediging, in een for loop gezet omdat het makkelijker is om te lezen
        for key, action in defense_options.items():
            slow_print(f"  {key}. {action}")  # laat de opties zien
            newturn.play()  # geluid voor elke optie

        choice = input("Your choice (1-4): ").strip()  # vraagt om een keuze van de speler

        # keuze verwerking
        if choice not in defense_options:
            slow_print("Invalid choice! You lose this turn.")  # als je niet tussen 1 en 4 kiest, krijg je
            wall_hp -= attack  # de schade die de commandant doet
        else: # als je wel tussen 1 en 4 kiest, dan krijg je de schade die werd berekend
            if name == "Ibrahim Pasha":
                wall_hp -= defend_ibrahim(choice, attack)
            elif name == "Evrenos":
                wall_hp -= defend_evrenos(choice, attack)
            elif name == "Haim Fahri":
                wall_hp -= defend_haim(choice, attack)
            elif name == "Omer Pasha":
                wall_hp -= defend_omer(choice, attack)
            elif name == "Sultan Mehmet II":
                wall_hp -= defend_sultan()

        turn += 1  # verhoogt de beurt met 1
        time.sleep(2)  # wacht twee secondes voor de volgende beurt

    # als de muur hp 0 is
    slow_print("\nThe wall has fallen. Constantinople is lost...")
    slow_print("The Eastern Roman Empire has come to an end.")
    bgsong.stop()  # stopt de achtergrond muziek
    lose_sound.play()
    time.sleep(30)  # paar secondjes wachten voor het spel beeindigt