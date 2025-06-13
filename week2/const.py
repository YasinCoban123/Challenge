import random
import time
from time import sleep
import pygame 

pygame.mixer.init()

intromelody = pygame.mixer.Sound("soundw2/intromelody.mp3")
bgsong = pygame.mixer.Sound("soundw2/0414.MP3")
newturn = pygame.mixer.Sound("soundw2/newturn.mp3")
wall_damage = pygame.mixer.Sound("soundw2/wall_damage.mp3")
win_sound = pygame.mixer.Sound("soundw2/bgsong4.mp3")
lose_sound = pygame.mixer.Sound("soundw2/endsong.mp3") 

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

# Class voor elke commandant
class Commander:
    def __init__(self, name, attack_range, weak_defense=None):
        self.name = name
        self.low, self.high = attack_range
        self.weak_defense = weak_defense

    def get_attack(self):
        return random.randint(self.low, self.high)

    def calculate_damage(self, choice, attack):
        if self.weak_defense and choice == self.weak_defense:  # als de speler de juiste verdediging kiest
            slow_print(f"You countered {self.name} effectively!")
            damage = int(attack * 0.5)
        else:
            slow_print(f"{self.name} breaks through your defenses!")  # incorrecte verdediging
            damage = attack
        slow_print(f"The wall takes {damage} damage.")  # laat zien hoeveel schade er is gedaan
        wall_damage.play()
        return damage  # geeft de schade terug

# de vijf vijanden die in de spel zijn, met hun zwakke verdediging (behalve Sultan)
commanders = {
    "Ibrahim Pasha": Commander("Ibrahim Pasha", (100, 200), "4"),
    "Evrenos": Commander("Evrenos", (50, 100), "1"),
    "Haim Fahri": Commander("Haim Fahri", (30, 60), "2"),
    "Omer Pasha": Commander("Omer Pasha", (70, 120), "3"),
    "Sultan Mehmet II": Commander("Sultan Mehmet II", (250, 250))  # geen zwakte
}

# beginwaardes vastzetten
wall_hp = 1000
turn = 1 
pope_response_turn = random.randint(5, 10)  # 50/50 kans dat de pope helpt tussen beurt 5 en 10

# functie die een random commandant pakt uit de dict
def get_commander():
    name = random.choice(list(commanders.keys()))  # pakt een random naam uit de dict
    commander = commanders[name]
    attack = commander.get_attack()  # gebruikt random om te kiezen tussen de twee waardes
    return commander, attack  # geeft de commandant en aanval terug

# main game
def constantinople():
    global wall_hp, turn  # global om de vastgestelde waardes hier te gebruiken

    game_intro()  # speelt de intro functie
    bgsong.set_volume(0.7) 
    bgsong.play(-1)  # -1 zodat die in een loop blijft spelen

    # while loop die doorgaat totdat de muur hp 0 is
    while wall_hp > 0:
        slow_print(f"\nTurn {turn}")  # laat de huidige beurt zien, /n voor een nieuwe regel
        slow_print(f"Wall HP: {wall_hp}")  # laat de muur hp zien

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

        commander, attack = get_commander()  # pakt de random commandant en aanval
        slow_print(f"\nOttoman commander: {commander.name} is attacking!")  # laat zien wie er aanvalt
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
        else:  # als je wel tussen 1 en 4 kiest, dan krijg je de schade die werd berekend
            if commander.name == "Sultan Mehmet II":
                slow_print("Sultan Mehmet II cannot be defended against, he strikes furiously.")  # De sultan kan niet worden tegengehouden
                wall_damage.play()
                wall_hp -= 250  # returned 250 schade aan de wall
            else:
                wall_hp -= commander.calculate_damage(choice, attack)

        turn += 1  # verhoogt de beurt met 1
        time.sleep(2)  # wacht twee secondes voor de volgende beurt

    # als de muur hp 0 is
    slow_print("\nThe wall has fallen. Constantinople is lost...")
    slow_print("The Eastern Roman Empire has come to an end.")
    bgsong.stop()  # stopt de achtergrond muziek
    lose_sound.play(-1)
    time.sleep(30)  # paar secondjes wachten voor het spel beeindigt