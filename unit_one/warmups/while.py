num = 1
#casts from string to int
user_guess = int(input("Guess a number"))

#repeats guessing command until right
while num != user_guess:
    print("Wrong, try again")
    if user_guess > num:
        print("too high")
        user_guess = int(input("guess a num from 0-100\n"))
    elif user_guess < num:
            user_guess = int(input("guess a num from 0-100\n"))

if num == user_guess:
    print("Congratulations you got it!")
