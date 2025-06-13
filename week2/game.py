from time import sleep
import pygame
import random


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pyramids = pygame.image.load("imagesw2/pyramids.jpeg")
spirit = pygame.image.load("imagesw2/spirit.jpeg")
shadow = pygame.image.load("imagesw2/shadowy_figure.jpg")
menu = pygame.image.load("imagesw2/menu_egypt.webp")
final_door = pygame.image.load("imagesw2/final_door.png")
inventory = []
player_path = ""
completed_pyramids = {
    "Khafre": False,
    "Menkaure": False,
}

def print_slow(text, delay=0.03): 
    for char in text:
        print(char, end='', flush=True)
        pygame.event.pump()  
        sleep(delay)
    print()  

def The_Great_pyramid():
    print_slow("You stand before the towering Great Pyramid of Giza, its ancient stones whispering secrets of the past.")
    print_slow("Do you:")
    print_slow("1. Enter the main chamber.")
    print_slow("2. Climb to the apex.")
    pygame.event.pump()
    choice = input("> ")

    if choice == "1":
        pygame.mixer.music.load("soundw2/footsteps.mp3")
        pygame.mixer.music.play()
        print_slow("Inside, hieroglyphs shimmer faintly. A chill runs down your spine.")
        print_slow("You find an Ancient Amulet on a pedestal.")
        inventory.append("Ancient Amulet")
    elif choice == "2":
        screen.fill((0, 0, 0))
        screen.blit(pyramids, (0, 0))
        pygame.display.update()
        print_slow("The climb is treacherous, but the view reveals the layout of the pyramid complex.")
        input("Press Enter to continue...")
    else:
        print_slow("Confused by the choice, you hesitate and feel a cold presence pass through you...")

def The_Pyramid_of_Khafre():
    pygame.mixer.music.load("soundw2/footsteps.mp3")
    print_slow("The Pyramid of Khafre looms ahead, its entrance partly collapsed.")
    print_slow("Do you:")
    print_slow("1. Squeeze through the rubble.")
    print_slow("2. Search around the base.")
    pygame.event.pump()
    choice = input("> ")

    if choice == "1":
        print_slow("You crawl into a narrow passage, your torch flickering.")
        screen.fill((0, 0, 0))
        screen.blit(spirit, (0, 0))
        pygame.display.update()
        pygame.mixer.music.load("soundw2/ghost_whisper.mp3")
        pygame.mixer.music.play()
        print_slow("Inside, a ghostly guardian appears, offering a riddle.")
        print_slow("\"I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?\"")
        answer = input("Answer: ").lower()
        if "echo" in answer:
            print_slow("The spirit nods solemnly and fades, revealing a Golden Scarab.")
            inventory.append("Golden Scarab")
        else:
            print_slow("The spirit wails and vanishes. The passage trembles. You retreat.")
    elif choice == "2":
        print_slow("Among the sand and stone, you discover a hidden chamber.")
        print_slow("Inside lies the Pharaoh’s Seal.")
        inventory.append("Pharaoh’s Seal")
    else:
        print_slow("Paralyzed by indecision, a sandstorm forces you to flee...")

def continue_khafre_path():
    pygame.mixer.music.load("soundw2/footsteps.mp3")
    pygame.mixer.music.play()
    print_slow("Venturing deeper into Khafre, you hear whispers echoing through the halls.")
    print_slow("A riddle is etched in blood on the wall:")
    print_slow("\"I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?\"")
    pygame.event.pump()
    answer = input("Answer: ").lower()
    if "map" in answer:
        print_slow("A hidden door creaks open, revealing the Obsidian Dagger.")
        inventory.append("Obsidian Dagger")
    else:
        print_slow("The walls seem to close in. You turn back before it’s too late.")

def heart_of_khafre():
    print_slow("You reach the heart of the pyramid, where darkness clings like cobwebs.")
    print_slow("A glowing urn sits atop a stone altar.")
    print_slow("As you approach, a shadowy figure rises, eyes burning with malice.")
    
    screen.fill((0, 0, 0))
    screen.blit(shadow, (0, 0))
    pygame.display.update()
    
    print_slow("Do you:")
    print_slow("1. Confront the figure.")
    print_slow("2. Attempt to sneak past.")
    pygame.event.pump()
    choice = input("> ")

    if choice == "1":
        print_slow("You brandish a relic. The figure recoils, then dissipates into dust.")
        print_slow("You take the Enchanted Urn.")
        inventory.append("Enchanted Urn")
    elif choice == "2":
        print_slow("You tiptoe around, but your foot snaps a bone.")
        print_slow("The figure screeches and vanishes, leaving the urn behind in rage.")
        inventory.append("Enchanted Urn")
    else:
        print_slow("Frozen in fear, the figure vanishes, taking the urn with it...")

def The_Pyramid_of_Menkaure():
    print_slow("Smaller but no less eerie, the Pyramid of Menkaure beckons.")
    print_slow("Inside, tunnels branch in every direction.")
    print_slow("You follow the path where air is thickest with age.")
    print_slow("On a stone plinth lies a Jackal Idol. Do you take it? (yes/no)")
    pygame.event.pump()
    choice = input("> ").lower()
    if choice == "yes":
        pygame.mixer.music.load("soundw2/pulse.mp3")
        pygame.mixer.music.play()
        print_slow("As your fingers touch it, the walls pulse with energy.")
        inventory.append("Jackal Idol")
    else:
        print_slow("You leave it untouched, a whisper trailing behind you...")

    print_slow("Further in, a faint humming guides you to a chamber with a feather floating mid-air.")
    print_slow("This is no ordinary feather—it is obsidian black and impossibly heavy.")
    inventory.append("Obsidian Feather")

    print_slow("In the final chamber, a Crystal Ankh rests in a shaft of light.")
    print_slow("As you lift it, the walls groan in warning.")
    inventory.append("Crystal Ankh")

    print_slow("On your way out, you stumble over a stone fragment etched with a sun symbol.")
    inventory.append("Sun Disk Fragment")

def check_final_door():
    print_slow("You return to the sealed chamber in the Great Pyramid.")
    print_slow("The final door looms before you, engraved with five sockets.")
    required_items = {"Ancient Amulet", "Golden Scarab", "Pharaoh’s Seal", "Obsidian Dagger", "Enchanted Urn"}

    if required_items.issubset(set(inventory)):
        print_slow("Each item fits perfectly into place...")
        pygame.mixer.music.load("soundw2/final_door_opening.mp3")
        
        screen.fill((0, 0, 0))
        screen.blit(final_door, (0, 0))
        pygame.display.update()

        print_slow("With a low rumble, the door opens to reveal a chamber filled with golden light.")
        print_slow("A deep voice speaks to you and says")
        print_slow("You have given what was taken, now take what was given")
        print_slow("You have uncovered the secret of Horror Egypt.")
        print_slow("You're amazed and feel honored, but you feel like this is a trap.")
        print_slow("Do you trust it and go in or do you escape?")
        pygame.event.pump()
        choice = input("> yes/no ")
        if choice == "yes":
            print_slow("You solved many riddles to get here.")
            print_slow("You deserve the rewards that are inside, so you decide to go in")
            pygame.mixer.music.load("soundw2/deep_voice.mp3")
            pygame.mixer.music.play()
            print_slow("The deep voice lets out a big roar and says")
            print_slow("You have failed the final test, greed is what has consumed you")
            print_slow("You turn to dust and become a curse wandering inside the pyramid")
            print_slow("Bad Ending")
        elif choice == "no":
            print_slow("You decide to leave the treasure and artifacts and head back home and report.")
            print_slow("The deep voice says")
            print_slow("Congratulations, you have succeeded mortal. You have no desire except for knowledge and gifts you one of his artifacts")
            print_slow("You tremble and thank the voice, wondering what would have happened if you had gone in")
            print_slow("Good Ending")
    else:
        print_slow("The door remains shut. You are missing something vital...")
        print_slow("The spirits stir uneasily. You must find all five artifacts.")

def horror_egypt():
    pygame.mixer.music.load("soundw2/backgroundmusic.mp3")
    pygame.mixer.music.play(-1)
    screen.blit(menu, (0, 0))
    pygame.display.update()
    global inventory, player_path, completed_pyramids
    print_slow("Welcome to Horror Egypt.\n")
    print_slow("You are Samir, an archaeologist exploring ancient Egyptian pyramids.")
    print_slow("Your goal is to uncover the secrets within and find your way to the final door in the Great Pyramid.\n")
    showing_menu = True
    while showing_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                showing_menu = False  
    while True:
        print_slow("\nChoose your path:")
        print_slow("[1] Enter The Great Pyramid")
        print_slow("[2] Enter The Pyramid of Khafre")
        print_slow("[3] Enter The Pyramid of Menkaure")
        print_slow("[4] Check Final Door")
        print_slow("[5] View Inventory")
        print_slow("[6] Quit")

        pygame.event.pump()
        choice = input("> ")
        if choice == "1":
            The_Great_pyramid()
        elif choice == "2":
            The_Pyramid_of_Khafre()
            continue_khafre_path()
            heart_of_khafre()
            completed_pyramids["Khafre"] = True
        elif choice == "3":
            The_Pyramid_of_Menkaure()
            completed_pyramids["Menkaure"] = True
        elif choice == "4":
            check_final_door()
        elif choice == "5":
            print_slow("Inventory:")
            for item in inventory:
                print_slow(f"- {item}")
        elif choice == "6" or choice.lower() == "quit":
            print_slow("Farewell, explorer.")
            break
        else:
            print_slow("Invalid choice. Try again.")


def japan():
    print_slow("""The year is 1367, and you are Nagasaki, one of the most notorious samurai.
The Shogun has commanded you to eliminate all of the Mongolian raiding camps and villages.
#################################################
P.S. This is a short turn-based fighting game.
""")
    print_slow("You approach the Mongolian camp. A fierce Mongolian warrior steps forward to challenge you!")
    
    # Initial stats
    player_health = 100
    special_moves = 2
    level = 1
    player_damage = 15
    
    # Level up system
    def level_up():
        nonlocal player_health, player_damage, special_moves, level
        level += 1
        player_health += 30  
        player_damage += 5   
        special_moves += 1 
        print_slow(f"\nYou've leveled up to Level {level}!")
        print_slow(f"Your health is now {player_health}. Your damage is now {player_damage}. You can now use {special_moves} special moves!")
    
    # Enemy stats
    def enemy_stats(battle_number):
        if battle_number == 1:
            return 50, 10 
        elif battle_number == 2:
            return 70, 15  
        elif battle_number == 3:
            return 90, 20  
        else:
            return 120, 25  
    
    def boss_special_skill():
        print_slow("\nThe Mongolian boss roars and activates 'Mongolian Fury'!")
        fury_damage = random.randint(40, 60)
        print_slow(f"The boss strikes with overwhelming force, dealing {fury_damage} damage to you!")
        return fury_damage
    
    for battle_number in range(1, 5):
        print_slow(f"\nBattle {battle_number}")
        
        enemy_health, enemy_damage = enemy_stats(battle_number)
        print_slow(f"A fierce Mongolian warrior appears! Enemy health: {enemy_health}, Enemy damage: {enemy_damage}")
        
        current_enemy_health = enemy_health
        
        while player_health > 0 and current_enemy_health > 0:
            print_slow(f"\nYour health: {player_health} | Enemy health: {current_enemy_health}")
            print_slow(f"Special moves remaining: {special_moves}")
            print_slow(f"Level: {level}")
            
            action = input("Do you want to (A)ttack, (D)efend, or (S)pecial move? ").lower()

            if action == 'a':
                damage = random.randint(player_damage, player_damage + 10)
                current_enemy_health -= damage
                print_slow(f"You attack the Mongolian warrior and deal {damage} damage!")
            elif action == 'd':
                defense = random.randint(5, 15)
                player_health += defense
                print_slow(f"You defend yourself, restoring {defense} health!")
            elif action == 's' and special_moves > 0:
                move_choice = input("Choose your special move: (1) Furious Strike, (2) Healing Surge: ").strip()
                if move_choice == '1':
                    damage = random.randint(30, 50)
                    current_enemy_health -= damage
                    print_slow(f"You unleash a Furious Strike and deal {damage} damage!")
                elif move_choice == '2':
                    heal = random.randint(20, 30)
                    player_health += heal
                    print_slow(f"You perform a Healing Surge, restoring {heal} health!")
                else:
                    print_slow("Invalid choice. No special move used.")
                    continue
                special_moves -= 1  
            else:
                print_slow("Invalid action. Choose again.")
                continue
            
            # Enemy attacks
            if current_enemy_health > 0:
                enemy_attack = random.randint(enemy_damage - 5, enemy_damage + 5)
                player_health -= enemy_attack
                print_slow(f"The Mongolian warrior attacks you and deals {enemy_attack} damage!")
        
        # Check if player should level up
        if current_enemy_health <= 0:
            print_slow(f"\nYou defeated the Mongolian warrior in battle {battle_number}!")
            level_up()  
            if battle_number < 3:
                continue  
            else:
                print_slow("You have reached the boss battle!")
                
                if player_health > 0:
                    boss_attack = boss_special_skill()
                    player_health -= boss_attack
                
                while player_health > 0:
                    print_slow(f"\nYour health: {player_health} | Boss health: {current_enemy_health}")
                    action = input("Do you want to (A)ttack, (D)efend, or (S)pecial move? ").lower()

                    if action == 'a':
                        damage = random.randint(player_damage, player_damage + 10)
                        current_enemy_health -= damage
                        print_slow(f"You attack the Mongolian boss and deal {damage} damage!")
                    elif action == 'd':
                        defense = random.randint(5, 15)
                        player_health += defense
                        print_slow(f"You defend yourself, restoring {defense} health!")
                    elif action == 's' and special_moves > 0:
                        move_choice = input("Choose your special move: (1) Furious Strike, (2) Healing Surge: ").strip()
                        if move_choice == '1':
                            damage = random.randint(30, 50)
                            current_enemy_health -= damage
                            print_slow(f"You unleash a Furious Strike and deal {damage} damage!")
                        elif move_choice == '2':
                            heal = random.randint(20, 30)
                            player_health += heal
                            print_slow(f"You perform a Healing Surge, restoring {heal} health!")
                        else:
                            print_slow("Invalid choice. No special move used.")
                            continue
                        special_moves -= 1 
                    else:
                        print_slow("Invalid action. Choose again.")
                        continue

                    if current_enemy_health > 0:
                        boss_attack = random.randint(enemy_damage - 5, enemy_damage + 5)
                        player_health -= boss_attack
                        print_slow(f"The Mongolian boss attacks you and deals {boss_attack} damage!")
                
                if player_health > 0:
                    print_slow("\nYou have defeated the Mongolian boss! Victory is yours!")
                else:
                    print_slow("\nYou have been defeated by the Mongolian boss. The Mongol raiders win this day.")
                break