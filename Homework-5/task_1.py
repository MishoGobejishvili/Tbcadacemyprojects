
# 1. დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n , სადაც 0 < n < 50 .
# Პროგრამამ უნდა იპოვოს n მდე არსებული ყველა რიცხვის გამყოფები. Დაბეჭდეთ მაქსიმუმ 3 ცალი გამყოფი.

n = int(input("Enter number: "))

if 0 < n < 50:
    for i in range(1, n + 1):
        count = 0
        print(str(i), end=" - ")
        for j in range(1, n + 1):
            if count != 3 and i % j == 0:
                count += 1
                print(str(j), end=" ")
        print()
else:
    print("Invalid input")
