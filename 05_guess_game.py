import random

num = random.randint(0,10)
guesses = 3
guess = int(input("You have three chances to guess the number I'm thinking about between 0 and 10. What's your guess? ") )


while guesses > 0:
    guesses = guesses - 1
    while True:
        if guess == num:
            break
        else:
            guess = int(input("Nope. Try again. You have " + str(guesses) + " guesses left."))
    print("You guessed it. I was thinking about",str(num)+".")

print("Sorry, you've run out of guesses.")
