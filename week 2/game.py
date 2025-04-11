from time import sleep
import pygame
import random

pygame.mixer.init()

inventory = []
player_path = ""
completed_pyramids = {
    "Khafre": False,
    "Menkaure": False,
}

def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.10)
    print()

def The_Great_pyramid():
    global inventory, player_path

    print("\nYou enter The Great Pyramid and feel a slight, menacing breeze.")
    sleep(1)
    print("You see that there are two paths.")
    print("The left path leads down a dark, spiraling stairway.")
    print("On the right, you see a flickering torch illuminating an entrance blocked by spiderwebs.\n")
    sleep(2)

    choice = input("Which way do you choose?\n[1] Left (toward darkness)\n[2] Right (toward the torch)\n> ")

    if choice == "1":
        print("\nYou descend the dark stairway, the air growing colder with each step.")
        sleep(2)
        print("You enter a circular chamber. Strange glyphs glow faintly on the wall.")
        print("A voice seems to echo in your mind: 'Only those who understand may see what was.'\n")
        sleep(2)

        print("A puzzle appears:\n")
        print("Riddle: I am not alive, but I grow. I don't have lungs, but I need air. What am I?")
        answer = input("> ").lower()

        if "fire" in answer:
            print("\nThe glyphs pulse with light. You hear a deep *click* behind the wall.")
            print("A hidden door slides open, revealing a passage even deeper.")
            player_path = "solver"
            sleep(2)
            continue_left_path()
        else:
            print("\nThe glyphs dim. The room grows colder...")
            print("A ghostly scream echoes through the chamber. You run back the way you came.")
            return

    elif choice == "2":
        print("\nYou brush past the thick webs and enter a narrow hallway.")
        sleep(2)
        print("Lying in the dust is a small, jade scarab. Its eyes seem to shimmer as you approach.")
        take = input("Do you take the scarab? [yes/no] > ").lower()

        if take == "yes":
            print("\nYou pocket the scarab. A distant grinding sound echoes...")
            inventory.append("Scarab")
        else:
            print("\nYou leave the scarab untouched, though its gaze lingers.")

        sleep(2)
        print("\nYou move deeper and arrive at a hall lined with jackal-headed statues.")
        print("One holds a stone bowl. An inscription reads:\n")
        print("'To pass, give what is taken. To take, give what is hidden.'\n")

        choice2 = input("Do you [1] place an item in the bowl or [2] try to sneak past the statues?\n> ")

        if choice2 == "1":
            if "Scarab" in inventory:
                print("\nYou place the scarab in the bowl. The statues lower their heads in silent approval.")
                print("A wall opens, revealing a passage forward.")
                inventory.remove("Scarab")
                sleep(2)
                continue_right_path()
            else:
                print("\nYou have nothing to offer. The statues’ eyes glow red...")
                print("You flee back the way you came.")
                return
        elif choice2 == "2":
            print("\nYou attempt to sneak past...")
            sleep(2)
            print("But the floor shifts. You trigger a trap and barely escape with your life!")
            print("Breathing heavily, you stumble into a side tunnel.")
            player_path = "explorer"
            sleep(2)
            continue_right_path()
        else:
            print("\nYou hesitate — and the statues begin to move. You run.")
            return
    else:
        print("\nYou hesitate too long. A low rumble shakes the floor. You must choose quickly next time.")
        return


def continue_left_path():
    print("\nYou crawl through the secret tunnel and drop into a chamber lit by sourceless light.")
    sleep(2)
    print("In the center lies a cracked sarcophagus. Dust swirls unnaturally around it.\n")
    choice = input("Do you [1] approach the sarcophagus or [2] search the walls? > ")

    if choice == "1":
        print("\nYou approach carefully. The sarcophagus is empty... except for claw marks on the inside.")
        print("A chill crawls up your spine. Something was trapped here once.")
    elif choice == "2":
        print("\nYou examine the walls and find a hidden switch.")
        print("A passage opens — leading to a chamber pulsing with ancient power.")
        inventory.append("Crystal Ankh")
        print("\nYou have found the Crystal Ankh! It radiates with a soft, otherworldly glow.")
    else:
        print("\nFrozen in fear, you wait. The air grows heavier...")

    sleep(2)
    heart_of_the_pyramid(player_path)


def continue_right_path():
    print("\nYou descend deeper into the pyramid’s forgotten heart.")
    sleep(2)
    print("Obsidian walls rise around you, etched with silver symbols glowing faintly.")
    sleep(2)
    heart_of_the_pyramid(player_path)


def heart_of_the_pyramid(path_type):
    print("\nYou have arrived at the Heart of the Pyramid.")
    sleep(2)

    if path_type == "solver":
        print("\n A voice whispers from the glyphs: 'You are the Solver. Mind over fear. Logic over death.'")
    elif path_type == "explorer":
        print("\n A voice rises from the stones: 'You are the Explorer. Brave in shadow. Bold in silence.'")

    sleep(2)
    print("\nA massive black door looms ahead. Five recesses are carved into its surface.")
    print("Each shaped to fit a unique offering.")

    required_items = [
        "Scarab",
        "Jackal Idol",
        "Obsidian Feather",
        "Crystal Ankh",
        "Sun Disk Fragment"
    ]

    offered_items = [item for item in required_items if item in inventory]

    if len(offered_items) == 5:
        print("\n✨ The items glow as you approach. The door opens slowly with a grinding roar.")
        print("You step forward into something... ancient, alive, and waiting.")
    else:
        print(f"\nThe door remains sealed. You have {len(offered_items)} of the 5 required items.")
        print("A voice speaks: 'Only when all offerings are gathered shall the path open.'")
        print("You must return to the other pyramids to complete your journey.")


def The_Pyramid_of_Khafre():
    global inventory, player_path
    
    print("\nYou step into the shadow of the Pyramid of Khafre, a place where darkness seems to pulse with life.")
    sleep(2)
    print("The air is thick, filled with an unnatural chill. The whispers of long-dead souls echo faintly.")
    print("You see two paths: one leads to a dark hallway, and the other seems to be a grand chamber with flickering light.")
    sleep(2)

    choice = input("Which way do you choose?\n[1] Dark hallway\n[2] Grand chamber\n> ")

    if choice == "1":
        print("\nYou venture down the dark hallway, the walls etched with strange symbols. The whispers grow louder.")
        sleep(2)
        print("Suddenly, the air shifts, and you feel a cold presence behind you.")
        print("A ghostly figure materializes in front of you, its eyes glowing a faint blue.")
        print("It speaks in a cryptic voice: 'What price will you pay to enter the land of the dead?'")
        
        answer = input("Do you [1] Offer an item or [2] Decline the spirit? > ")

        if answer == "1":
            print("\nThe spirit nods, its form flickering. It grants you a passage deeper into the pyramid.")
            inventory.append("Jackal Idol")
            player_path = "khafre_spirit"
            continue_khafre_path()

        else:
            print("\nThe spirit's eyes darken. It warns you of the dangers ahead but lets you pass.")
            player_path = "khafre_spirit"
            continue_khafre_path()

    elif choice == "2":
        print("\nYou step into a vast chamber, the walls adorned with ancient symbols and rituals.")
        sleep(2)
        print("At the center, a large altar is bathed in dim, flickering light. The air smells faintly of incense.")
        print("An inscription on the altar reads: 'Only through the pact can one pass beyond death.'")
        
        choice2 = input("Do you [1] Investigate the altar or [2] Search the surrounding artifacts? > ")

        if choice2 == "1":
            print("\nYou approach the altar. The moment you touch it, a surge of energy runs through you.")
            print("A ghostly figure appears, saying: 'You now bear the mark of Khafre's curse.'")
            inventory.append("Sun Disk Fragment")
            player_path = "khafre_ritual"
            continue_khafre_path()
        else:
            print("\nYou find a hidden artifact beside the altar. It's a cursed amulet glowing with dark energy.")
            print("It seems to resonate with the spirit world, but touching it fills you with dread.")
            inventory.append("Cursed Amulet")
            player_path = "khafre_artifacts"
            continue_khafre_path()

    else:
        print("\nYou hesitate too long, and the spirits of the pyramid grow restless. A loud rumble shakes the walls!")
        return


def continue_khafre_path():
    print("\nYou venture deeper into the pyramid, following the path that has opened before you.")
    sleep(2)
    print("The air thickens, and you sense you're approaching the heart of Khafre's dark pact.")
    sleep(2)
    heart_of_khafre(player_path)

def heart_of_khafre(path_type):
    print("\nThe air is dense, filled with the scent of ancient dust.")
    if path_type == "khafre_spirit":
        print("The spirit of Khafre's legacy calls to you, and the air grows colder with each step.")
    elif path_type == "khafre_artifacts":
        print("The cursed amulet weighs heavily around your neck as you enter the inner sanctum.")
    elif path_type == "khafre_ritual":
        print("The ancient ritual is almost complete, and the walls pulse with dark energy.")

    sleep(2)
    print("\nA massive, intricate door stands before you.")
    print("It has five carved recesses, each holding a different symbol... one that matches the items you have gathered.")
    sleep(2)

    check_final_door()

def check_final_door():
    print("\nYou approach the massive door, and it responds to the artifacts you have collected.")
    heart_of_the_pyramid(player_path)


def The_Pyramid_of_Menkaure():
    global inventory, player_path
    
    print("\nYou enter the Pyramid of Menkaure, the air thick with the scent of decay and ancient dust.")
    sleep(2)
    print("The walls are adorned with carvings of animals and gods, their eyes following your every movement.")
    print("You see two paths: one leads to a spiral staircase, and the other to a darkened chamber.\n")

    choice = input("Which way do you choose?\n[1] Spiral staircase\n[2] Darkened chamber\n> ")

    if choice == "1":
        print("\nYou begin climbing the spiral staircase, each step echoing in the silence.")
        sleep(2)
        print("At the top, you find a chamber with a large stone table.")
        print("A deep voice echoes in the air: 'You are here to claim your prize... or your curse.'")
        sleep(2)

        choice2 = input("Do you [1] investigate the table or [2] look for another exit? > ")

        if choice2 == "1":
            print("\nYou approach the stone table and find a glowing artifact — the Obsidian Feather.")
            inventory.append("Obsidian Feather")
            print("\nYou take the feather and hear the soft rustling of wind. The room grows colder.")
            player_path = "menkaure_find"
            continue_menkaure_path()
        else:
            print("\nYou find a narrow passage and make your way deeper into the pyramid.")
            player_path = "menkaure_escape"
            continue_menkaure_path()

    elif choice == "2":
        print("\nYou step into the darkened chamber, feeling the oppressive weight of ancient magic.")
        sleep(2)
        print("In the center, a pedestal rises from the floor, a small, golden artifact resting upon it.")
        print("A voice whispers: 'This is the key to your survival.'")
        
        choice2 = input("Do you [1] take the artifact or [2] leave it behind? > ")

        if choice2 == "1":
            print("\nYou take the artifact, and the room fills with an unsettling silence.")
            inventory.append("Golden Artifact")
            print("\nYou feel a strange power emanating from it as you leave the chamber.")
            player_path = "menkaure_key"
            continue_menkaure_path()
        else:
            print("\nYou leave the artifact untouched. The room shifts as if disappointed.")
            player_path = "menkaure_no_key"
            continue_menkaure_path()

    else:
        print("\nYou hesitate too long, and the pyramid begins to rumble!")
        return


def continue_menkaure_path():
    print("\nYou proceed deeper into the heart of Menkaure's pyramid.")
    sleep(2)
    heart_of_menkaure(player_path)


def heart_of_menkaure(path_type):
    print("\nThe pyramid's heart feels alive, pulsating with energy.")
    if path_type == "menkaure_find":
        print("You feel the presence of something ancient, watching your every move.")
    elif path_type == "menkaure_escape":
        print("You feel the weight of unseen eyes upon you.")
    elif path_type == "menkaure_key":
        print("You feel the power of the artifact growing stronger with each step.")
    elif path_type == "menkaure_no_key":
        print("The pyramid seems to grow more hostile, as if judging you.")

    sleep(2)
    print("\nA large door appears in front of you, its surface covered with symbols.")
    sleep(2)

    check_final_door() 

def horror_egypt():
    pygame.mixer.music.load("soundw2/backgroundmusic.mp3")
    pygame.mixer.music.play(-1)
    global inventory, player_path, completed_pyramids
    print_slow("Welcome to Horror Egypt.\n")
    print_slow("You are Samir, an archaeologist exploring ancient Egyptian pyramids.")
    sleep(2)
    print_slow("Your goal is to uncover the secrets within and find your way to the final door in the Great Pyramid.\n")
    
    while True:
        print("Choose your first path:")
        print("[1] Enter The Great Pyramid")
        print("[2] Enter The Pyramid of Khafre")
        print("[3] Enter The Pyramid of Menkaure")
        
        choice = input("> ")
        if choice == "1":
            The_Great_pyramid()
        elif choice == "2":
            The_Pyramid_of_Khafre()
        elif choice == "3":
            The_Pyramid_of_Menkaure()
        else:
            print("\nInvalid choice. Try again.")

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