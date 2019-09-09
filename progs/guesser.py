import random
r = random.randint(0,100)
print("I have thought of a number. Its your turn to guess!")

guesses = []
while True:
    guess = int(input("Enter your guess[0,100]: "))
    guesses.append(guess)
    if guess < r:
        print("Low")
    elif guess > r:
        print("High")
    else:
        print("Bingo! You guessed it right.")
        print("You took", len(guesses), "tries")
        print("These were your guesses -->", guesses)
        break
        