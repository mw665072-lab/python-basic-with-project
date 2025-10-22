import random

print("""Please Guess a random number either it is close to the number of not lets Fun Begin from 0 to 30""")
random_number = random.randint(0,30)
guess = 0
tries = 0
while guess != random_number:
    guess = int(input("\nEnter Guess Number "))
    if guess > 30:
        print("Guess number must be 0 to 30 ")
    else:
        if guess > random_number:
            print("Try Again number is greater then actual number")
            tries = tries + 1
        elif guess < random_number:
            print("Try Again number is less then actual number")
            tries = tries + 1
        else:
            if tries > 10:
                print("Congratulations You Guess the Exact number in", tries, "Tries Too Bad")
            elif tries > 5:
                print("Congratulations You Guess the Exact number in", tries, "Tries That's Goog")
            else:
                print("Congratulations You Guess the Exact number in", tries, "Tries Perfect")


