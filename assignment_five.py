import random


def play():
    play = input("Shall we play a game?")
    if play == "yes" or play == "Yes":
        return True
    elif play == "no" or play == "No":
        print("Okay fine, I didn't want you to play anyways!")
    else:
        return False


def draw():
    number = random.randint(1, 100)
    print(number)
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

            print("Finished")


main()
