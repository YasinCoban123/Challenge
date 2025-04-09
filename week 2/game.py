from time import sleep
import pygame

pygame.mixer.init()

pygame.mixer.music.load("backgroundmusic.mp3")
pygame.mixer_music.play(-1, 0.0)
pygame.mixer.music.set_volume(1.0)
inventory = []
player_path = ""


def print_slow(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.08)
    print()


def The_Great_pyramid():
    global inventory, player_path

    print_slow("\nYou enter The Great Pyramid and feel a slight, menacing breeze.")
    print_slow("You see that there are two paths.")
    print_slow("The left path leads down a dark, spiraling stairway.")
    print_slow("On the right, you see a flickering torch illuminating an entrance blocked by spiderwebs.\n")
    sleep(2)

    choice = input("Which way do you choose?\n[1] Left (toward darkness)\n[2] Right (toward the torch)\n> ")

    if choice == "1":
        print_slow("\nYou descend the dark stairway, the air growing colder with each step.")
        sleep(2)
        print_slow("You enter a circular chamber. Strange glyphs glow faintly on the wall.")
        print_slow("A voice seems to echo in your mind: 'Only those who understand may see what was.'\n")
        sleep(2)

        print_slow("A puzzle appears:\n")
        print_slow("Riddle: I am not alive, but I grow. I don't have lungs, but I need air. What am I?")
        answer = input("> ").lower()

        if "fire" in answer:
            print_slow("\nThe glyphs pulse with light. You hear a deep *click* behind the wall.")
            print_slow("A hidden door slides open, revealing a passage even deeper.")
            player_path = "solver"
            sleep(2)
            continue_left_path()
        else:
            print_slow("\nThe glyphs dim. The room grows colder...")
            print_slow("A ghostly scream echoes through the chamber. You run back the way you came.")
            return

    elif choice == "2":
        print_slow("\nYou brush past the thick webs and enter a narrow hallway.")
        sleep(2)
        print_slow("Lying in the dust is a small, shiny amulet. Its seems to be pulsing as you approach.")
        take = input("Do you take the amulet? [yes/no] > ").lower()

        if take == "yes":
            print_slow("\nYou pocket the ancient amulet. A distant grinding sound echoes...")
            inventory.append("Ancient Amulet")
            sleep(2)
            print_slow("\nYou move deeper and arrive at a hall lined with jackal-headed statues.")
            print_slow("One holds a stone bowl. An inscription reads:\n")
            print_slow("'To pass, give what is taken. To take, give what is hidden.'\n")

            choice2 = input("Do you [1] place an item in the bowl or [2] try to sneak past the statues?\n> ")

            if choice2 == "1":
                if "Ancient Amulet" in inventory:
                    print_slow("\nYou place the amulet in the bowl. The statues lower their heads in silent approval.")
                    print_slow("A wall opens, revealing a passage forward.")
                    sleep(2)
                    continue_right_path()
                else:
                    print_slow("\nYou have nothing to offer. The statues' eyes glow red...")
                    print_slow("You flee back the way you came.")
                    return
            elif choice2 == "2":
                print_slow("\nYou attempt to sneak past...")
                sleep(2)
                print_slow("But the floor shifts. You trigger a trap and barely escape with your life!")
                print_slow("Breathing heavily, you stumble into a side tunnel.")
                player_path = "explorer"
                sleep(2)
                continue_right_path()
            else:
                print_slow("\nYou hesitate — and the statues begin to move. You run.")
                return
    else:
        print_slow("\nYou hesitate too long. A low rumble shakes the floor. You must choose quickly next time.")
        return


def continue_left_path():
    print_slow("\nYou crawl through the secret tunnel and drop into a chamber lit by sourceless light.")
    sleep(2)
    print_slow("In the center lies a cracked sarcophagus. Dust swirls unnaturally around it.\n")
    choice = input("Do you [1] approach the sarcophagus or [2] search the walls? > ")

    if choice == "1":
        print_slow("\nYou approach carefully. The sarcophagus is empty... except for claw marks on the inside.")
        print_slow("A chill crawls up your spine. Something was trapped here once.")
    elif choice == "2":
        print_slow("\nYou examine the walls and find a hidden switch.")
        print_slow("A passage opens — leading to a chamber pulsing with ancient power.")
        inventory.append("Ancient Power Artifact")
    else:
        print_slow("\nFrozen in fear, you wait. The air grows heavier...")

    sleep(2)
    heart_of_the_pyramid(player_path)


def continue_right_path():
    print_slow("\nYou descend deeper into the pyramids forgotten heart.")
    sleep(2)
    print_slow("Obsidian walls rise around you, etched with silver symbols glowing faintly.")
    sleep(2)
    heart_of_the_pyramid(player_path)


def heart_of_the_pyramid(path_type):
    print_slow("\nYou have arrived at the Heart of the Pyramid.")
    sleep(2)

    if path_type == "solver":
        print_slow("\nA voice whispers from the glyphs: 'You are the Solver. Mind over fear. Logic over death.'")
    elif path_type == "explorer":
        print_slow("\nA voice rises from the stones: 'You are the Explorer. Brave in shadow. Bold in silence.'")

    sleep(2)
    print_slow("\nA massive black door looms ahead. Five recesses are carved into its surface.")
    print_slow("Each shaped to fit a unique offering.")

    required_items = [
        "Ancient Amulet", "Golden Scarab", "Pharaohs Seal",
        "Obsidian Dagger", "Enchanted Urn"]

    offered_items = [item for item in required_items if item in inventory]

    if len(offered_items) == 5:
        print_slow("\n✨ The items glow as you approach. The door opens slowly with a grinding roar.")
        print_slow("You step forward into something... ancient, alive, and waiting.")
    else:
        print_slow(f"\nThe door remains sealed. You have {len(offered_items)} of the 5 required items.")
        print_slow("A voice speaks: 'Only when all offerings are gathered shall the path open.'")
    sleep(2)


def final_door():
    print_slow("\nYou step into the heart of the Great Pyramid.")
    print_slow("A cold draft brushes your skin as torches ignite along the walls—one by one—illuminating an ancient chamber.")
    print_slow("At the center stands an enormous obsidian door, etched with glowing hieroglyphs pulsing with an eerie light.")
    print_slow("A deep rumble echoes as the door responds to your presence...")

    required_items = [
        "Ancient Amulet", "Golden Scarab", "Pharaoh's Seal",
        "Obsidian Dagger", "Enchanted Urn"
    ]

    missing_items = [item for item in required_items if item not in inventory]

    if not missing_items:
        print_slow("\nYour collected relics begin to vibrate in unison, rising from your satchel and floating toward the door.")
        print_slow("The hieroglyphs flare with golden light as each item embeds itself into the stone.")
        print_slow("With a final, thunderous crack—the door begins to open.")
        print_slow("\nInside lies a radiant chamber untouched by time. A sarcophagus rests beneath a pyramid of golden light.")
        print_slow("The spirit of the ancient Pharaoh appears, nodding solemnly.")
        print_slow("You have proven yourself worthy.")
        print_slow("The secrets of the ancients are now yours...\n")
        print_slow("✨ You have completed the journey. The curse is broken. ✨\n")
        print_slow("THE END")
    else:
        print_slow("\nThe door resists your attempt to open it.")
        print_slow("An invisible force repels you, and the chamber begins to shake violently.")
        print_slow("A voice echoes through the walls: 'Only those who bear the five sacred relics may proceed.'")
        print_slow("You are missing:")
        for item in missing_items:
            print_slow(f"- {item}")
        print_slow("\nThe torches extinguish, and darkness floods the chamber.")
        print_slow("You must return to the other pyramids and complete your quest.")


def horror_egypt():
    print_slow("""You are Samir, an adventurous archaeologist known for uncovering the most famous and iconic finds.
    But your next journey is like no other.
    The pyramids, a place that contains some of the most notorious mysteries that remain unsolved, await you.
    Press enter to continue""")

    input("Press Enter to start your adventure...")

    user = input("\nYou find yourself among the pyramids, but do not know which pyramid you enter first.\n[1] The Great Pyramid\n[2] The Pyramid of Khafre\n[3] The Pyramid of Menkaure\n> ")

    if user == "1":
        print_slow("\nThe long-forgotten Great Pyramid, rumored to be the tomb of a Pharaoh, calls to you.")
        The_Great_pyramid()
    elif user == "2":
        print_slow("\nYou decide to enter the Pyramid of Khafre.")
        sleep(2)
    else:
        print_slow("\nYou decide to explore the Pyramid of Menkaure.")
        sleep(2)


horror_egypt()
