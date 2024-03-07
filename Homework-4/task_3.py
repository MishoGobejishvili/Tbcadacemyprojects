
# 3. Დაწერეთ პროგრამა რომელიც მიიღებს მთელ დადებით რიცხვს. Პროგრამამ უნდა იპოვოს და ეკრანზე
# ერთ ხაზზე დაბეჭდოს ამ რიცხვის ყველა გამყოფი. 0 < n < 1000.
# Მაგალითად: Enter number: 18 1 2 3 6 9 18

number = int(input("Enter number: "))

if 0 < number < 1000:
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=" ")
else:
    print("Incorrect input. Enter number between 0 and 1000")
