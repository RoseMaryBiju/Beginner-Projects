import random

guesses = 0 

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("type a number larger than 0 ")
        quit()

else:
    print("please enter a number")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it correct")
        break
    elif  user_guess > random_number:
            print("you were above the number")
    else:
            print("you were below the number")
    
print("you got it in", guesses, "guesses")