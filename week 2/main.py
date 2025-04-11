from game import horror_egypt
from game import japan
from const import constantinople
from time import sleep
import pygame

pygame.mixer.init()

def slow_print(text, delay=0.06): 
    for char in text:
        print(char, end='', flush=True)  
        sleep(delay)
    print()  


def main():
    intromelody = pygame.mixer.Sound("soundw2/mainsong.mp3")
    intromelody.set_volume(0.8)
    intromelody.play()
    slow_print("Welkom naar de drie deuren. Voor je zie je drie scenarios. welke kies je?")
    slow_print("1. Constantinople")
    slow_print("2. Egypt")
    slow_print("3. Japan")

    choice = input("Choose a door: ")
    
    if choice == "1":
        intromelody.stop()
        constantinople()
    elif choice == "2":
        intromelody.stop()
        horror_egypt()
    elif choice == "3":
        intromelody.stop()
        japan()
    else:
        slow_print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()