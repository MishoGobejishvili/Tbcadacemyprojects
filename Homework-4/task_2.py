import random

# 2. დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს - n. Პროგრამამ,
# უნდა დააგენერიროს n ცალი შემთვევით მთელი რიცხვი 0 – 1000 დიაპაზონიდან და
# ეკრანზე დაბეჭდოს მათ შორის მაქსიმალური. 0 < n < 30.

n = int(input("Enter number: "))
max_number = 0

if 0 < n < 30:
    for i in range(n):
        random_number = random.randint(0, 1000)
        if random_number > max_number:
            max_number = random_number
    print(max_number)
else:
    print("Incorrect input. Enter number between 0 and 30")
