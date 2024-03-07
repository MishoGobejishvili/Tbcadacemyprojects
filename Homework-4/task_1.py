import random

# 1. დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას. Პროგრამამ თითოეული
# მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი კამათლების წყვილი და დაბეჭდოს ეკრანზე.
# Მაგალითად: Enter players number: 2 3 4 2 1


amount_of_players = int(input("Enter players number: "))

if amount_of_players > 0:
    for i in range(0, amount_of_players):
        print(f"Player {i + 1}: {random.randint(0, 6)}, {random.randint(0, 6)}")
else:
    print("Invalid input ")
