# 1. დაწერეთ პროგრამა რომელიც მიიღებს მიიღებს სტრიქონი და დაადგენს ეს ტექსტი არის თუ არა პალინდრომი.

user_input = input("Input: ")
user_input = user_input.lower()

for c in user_input.lower():
    if not ('a' <= c <= 'z'):
        user_input = user_input.replace(c, "")

if user_input[0:int(len(user_input) / 2)] == user_input[-1:-int(len(user_input) / 2) - 1: -1]:
    print("Is palindrome")
else:
    print("Is not palindrome")
