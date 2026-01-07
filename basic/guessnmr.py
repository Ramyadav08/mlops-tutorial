import random
def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts=0
    for i in range(1,101):
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if user_guess < number_to_guess:
            print(" lower!")
        elif user_guess > number_to_guess:
            print(" high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
guess_the_number()