import random
import time

def roulette_simulation():
    # Let's define the numbers on the wheel
    wheel_number = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

    # We choose a random number from the wheel
    extract_number = random.choice(wheel_number)

    return extract_number

def game():
    bill = float(input("Load the money: "))

    while bill > 0:
        print(f"Current account balance: {bill}")

        # Ask the user how much they want to bet
        bet = float(input("How much do you want to bet? "))

        # Check if the bet is valid
        if bet <= 0 or bet > bill:
            print("Invalid bet. Please enter a valid bet.")
            continue

        # Run the roulette simulation
        extract_number = roulette_simulation()

        # Ask the user to choose a number
        user_number = int(input("Choose a number from roulette (0-36): "))
        print("\nThe ball is spinning...") 
        time.sleep(1.3) # Create suspense - wait 1.3 seconds
        print("\nWait...\n")
        time.sleep(1.3) # Create suspense - wait 1.3 seconds
        

        # Check if the number drawn corresponds to the one chosen by the user
        if user_number == extract_number:
            print("You won! The number drawn is", extract_number, "\n")
            win = bet * 36  # If the number is correct, the win is 36 times the bet
        else:
            print("Sorry, you lost. The number drawn is", extract_number, "\n")
            win = - bet  # If the number is wrong, the bet is lost

        # Update the account balance
        bill += win

    print("Your account has gone to 0. The game is over.\n")
    regame = input("Do you want to play again? (y/n) ")
    if regame == "y":
        game()
    else:
        print("Thank you for playing. Until next time!")
if __name__ == "__main__":
    game()
