# 5. *დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10.
# Პროგრამამ უნდა დაბეჭდოს სურათზე მოცემული სტრუქტურა. Გამოიყენეთ while

n = int(input("Enter number: "))
spaces = 11

if 0 < n < 10:
    i = 0
    while i <= n:
        print(("  " * (n - i)), end="")
        k = i
        while k >= 0:
            print(str(k) + " ", end="")
            k -= 1
        j = 1
        while j <= i:
            print(str(j) + " ", end="")
            j += 1
        print()
        i += 1
else:
    print("Incorrect input")
    