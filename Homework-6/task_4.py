
# 4. *დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10.
# Პროგრამამ უნდა დაბეჭდოს სურათზე მოცემული სტრუქტურა. Გამოიყენეთ while

n = int(input("Enter number: "))
print_number = ""

if 0 < n < 10:
    i = 1
    while i <= n:
        print_number += str(i) + " "
        print(print_number, end=" ")
        i += 1
        print()
    i = n - 1
    while i > 0:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        i -= 1
        print()
else:
    print("Incorrect input")
