
# Დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს, დაადგენს პირველი რიცხვი არის თუ არა მეორე რიცხვის ჯერადი და დაბეჭდავს ეკრანზე. A რიცხვს ეწოდება B რიცხვის ჯერადი, თუ A = B * n,  სადაც n ნატურალური რიცხვია.

a = int(input("Enter number one: "))
b = int(input("Enter number one: "))

if a > 0 and b > 0:
    if b % a == 0:
        print("a is a multiple of b")
    else:
        print("a is not a multiple of b")
else:
    print("Numbers can't be negative")
