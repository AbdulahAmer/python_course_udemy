import random
colors = ['blue','grey','red','pink','black','green','gold','silver','orange','yellow']


while True:
    num = random.randint(0,len(colors)-1)
    color = colors[num]
    guess  = (input("Please pick a color from the list above: ").lower())

    while True:
        if color == guess:
            break
        else:
            guess  = (input("Incorrect. Try again. ").lower())

    print("You guessed it. I was thinking about",color)

    again  = input("Let's play again? Type 'no' to quit: ")

    if again.lower() == 'no':
        break

print("Fun game")

    
