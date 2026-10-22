import random

randomNumber = random.randrange(1, 100)
guess =7

print ("You have maximum 7 attemps to guess the number")
print ("The numbers will be from 1 to 100 and we will help u dicover it :)")

while(guess>0):
    try:
        number = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid Number.")
        continue

    print("Press 0 to exit the game.")

    if number == 0:
        print("You have exited the game.")
        break

    if number == randomNumber:
        print("Congratulations! You guessed the number correctly.")
        break

    guess -= 1

    if number < randomNumber:
        print("Your guess is too low.")

    elif number > randomNumber:
        print("Your guess is too high.")

    print(f"The number of guesses left is: {guess}")


if guess == 0:
    print(f"Sorry, you've used all your attempts. The correct number was {randomNumber}.")



