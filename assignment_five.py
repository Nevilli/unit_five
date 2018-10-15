import random


def play():
    play = input("Shall we play a game?")
    if play == "yes" or play == "Yes":
        return True
    else:
        return False


def draw():
    return random.randint(1, 100)


def main():
    while True:
        if play():
            total_guesses = 0
            number = draw()
            guess = int(input("Try to guess my number?"))
            total_guesses = total_guesses + 1
            if guess == number:
                print("You guessed it!")
                print("You guessed it in", total_guesses)
                break
            elif guess < number:
                print("Your guess was too low")
            else:
                print("Your guess was too high")

        else:
            print("Finished")


main()
