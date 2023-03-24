import random
num = random.randint(1,100)
chance = 5
attempt = 1
guess = int(input(f"Attempt {attempt}: Guess the number: "))
while  chance > 0:
    if guess > num :
        print("Go a little lower")
        chance -= 1
    elif guess < num:
        print("Go a little higher ")
        chance -= 1
    elif guess == num:
        print(f"Congratulations!.... you guessed it correcly ")
        print("Game over")
        break
    if attempt >= 5:
        print(f"You could not guess it, the number was {num}")
        break
    attempt += 1
    print(f"You have {chance} attempt remaining")
    guess = int(input(f"Attempt {attempt}: Guess again: "))