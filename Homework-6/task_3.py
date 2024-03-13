import random

# დაწერეთ პროგრამა რომელიც “ჩაიფიქრებს” მთელ რიცხვს 0-დან 100-მდე.
# Მომხმარებელმა უნდა შემოიყვანოს თავისი ვარიანტი ჩაფიქრებული რიცხვის.
# Თუ მომხმარებლის შემოყვანილი რიცხვი დაემთხვა პროგრამის ჩაფიქრებულ რიცხვს,
# დაბეჭდეთ You are winner. Თუ მომხმარებლის შემოყვანილი რიცხვი მეტია,
# კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ high. თუ მომხმარებლის შემოყვანილი რიცხვი ნაკლებია კომპიუტერის ჩაფიქრებულ რიცხვზე,
# დაბეჭდეთ low. Მომხმარებელს აქვს მაქსიმუმ 10 მცდელობა. Თუ მომხმარებელმა 10 მცდელბაში ვერ გამოიცნო რიცხვი, დაბეჭდეთ Computer is winner.

program_random = random.randint(0, 100)
user_random = int(input("Enter random number between 0 - 100: "))
tries = 1

if 0 < user_random < 100:
    while tries < 10:
        if user_random > program_random:
            print("high")
        elif user_random < program_random:
            print("low")
        else:
            print("You are winner")
            break

        user_random = int(input("Try again: "))
        tries += 1

    print("Random number was: " + str(program_random))
    if user_random != program_random:
        print("Computer is winner")
else:
    print("Incorrect input")
