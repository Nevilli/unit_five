# Liam Neville
# 10/18/18
# This program asks the user if they want to play the guessing game, if yes, they play the game, if no, they don't.
import random


def play():
    """
    This function determines whether the player wants to play the game or not
    :return: False is returned twice in case the player does not want to play
            True is returned if the player wants to play the guessing game
    """
    play1 = input("Shall we play a game?")
    if play1 == "yes" or play == "Yes":
        return True
    elif play1 == "no" or play1 == "No":
        print("Okay fine, I didn't want you to play anyways!")
        return False
    else:
        return False


def draw():
    """
    This draws the random number for the guessing game
    :return: number is returned so the main function can use the value
    """
    number = random.randint(1, 100)
    return number


def main():
    while True:
        if play():
            total_guesses = 0
            number = draw()
            while True:
                guess = int(input("Try to guess my number?"))
                total_guesses = total_guesses + 1
                if guess == number:
                    print("You guessed it!")
                    print("You guessed it in", total_guesses, "tries")
                    break
                elif guess < number:
                    print("Your guess was too low")

                else:
                    print("Your guess was too high")

        else:
            print("Finished")
            break


main()
