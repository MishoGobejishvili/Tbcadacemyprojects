
# 3. დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n, სადაც 0 < n < 50.
# Პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე სიმბოლოებით *, /, | და \ .

n = int(input("Enter number: "))
left_side = "/"
right_side = "\\"
middle = "|"
foundation = middle

if 0 < n < 50:
    for i in range(0, n + 1):
        if i == 0:
            print(" " * n + "*")
        elif i == n:
            print((" " * n) + foundation)
        else:
            print((" " * (n - i)) + (i * left_side) + foundation + (i * right_side))
else:
    print("Incorrect input")
