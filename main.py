import random

def guess_age():
    print("Welcome! I'm going to try to guess your age.")
    name = input("What's your name? ")

    low, high = 15, 30
    attempts = 5
    while attempts > 0:
        guess = random.randint(low, high)
        response = input(f"{name}, are you {guess} years old?: ").lower()

        if response == 'y':
            print(f"Hooray! {name} is {guess} years old!")
            break
        else:
            print("Rats.")
            hint = input("Am I too (high/low)? ").lower()
            if hint == "high":
                high = guess - 1
            elif hint == "low":
                low = guess + 1
        attempts -= 1
    else:
        print(f"Sorry, {name}, I couldn't guess your age!")

guess_age()
