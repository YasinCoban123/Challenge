from game import horror_egypt
from game import japan
from const import constantinople
from rome import gladiator_game


def main():
    print("Welcome to the game!")
    print("1. Constantinople")
    print("2. Egypt")
    print("3. Japan")
    print("4. Gladiator Game")

    choice = input("Choose a game: ")
    
    if choice == "1":
        constantinople()
    elif choice == "2":
        horror_egypt()
    elif choice == "3":
        japan()
    elif choice == "4":
        gladiator_game()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()