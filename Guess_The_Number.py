import random

    
def play_game():    
    # Introduction

    print("Welcome to 'Number Guessing Game' ")
    print()
    print("Level:")
    print("1. Easy (1 - 100)")
    print("2. Hard (1 - 1000)")
    print("3. Extreme (1 - 10000)")

    # Loop to choose difficulty level

    while True:
        try:
            choice = int(input("Choose your capacity : "))
            if choice in [1,2,3]:
                break
            else:
                print("Please choose within limits.")
        except ValueError:
            print("It cannot be a string value")

    # Generation of number based on level

    while True:
        if choice == 1: number = random.randint(1,100)
        elif choice == 2: number = random.randint(1,1000)
        elif choice == 3: number = random.randint(1,10000)
        count = 0

        print("\n----All The Best----\n")

    # Main Game loop

        while True:
            while True:
                try:
                    guess = int(input('Your Guess: '))
                    break
                except ValueError:
                    print("It should be a number.")

            if guess == number:
                count += 1
                print("---------------------------------------")
                print("Voila!! You guessed it correct!!!")
                print("Total Count : ",count)
                print("---------------------------------------")

                break
            elif guess != number:
                count += 1
                print("")
                if guess > number:
                    print("Nope,Its Incorrect :( Guess something Lower vv\n")
                elif guess < number:
                    print("Nope,Its Incorrect :( Guess something Higher ^^\n")
        break        


if __name__ == "__main__":
    play_game()

# Option to play again

while True:
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
       
# Restart the game
       
        print("\nRestarting the game...\n")
        play_game()
        break
    elif play_again in ['no', 'n']:
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


