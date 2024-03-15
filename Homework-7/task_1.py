import sys

# 1. დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 20.
# Პროგრამამ უნდა იპოვოს მიმდევრობის 0-დან n-მდე წევრები. Მიმდევრობა განისაზღვრება შემდეგნაირად:
# ნულოვანი წევრი არის 0, პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი.
# გამოიყენეთ while ციკლი და არ შეიძლება list-ის გამოყენება. Მაგალითი:

n = int(input("Enter number: "))
last_item = 1
before_last_item = 0
summary = 0
i = 0

if not (0 <= n < 20):
    print("Invalid input")
    sys.exit(1)

while summary < n:
    if i % 2 == 0:
        before_last_item = summary
        print(before_last_item, end=" ")
    else:
        last_item = summary
        print(last_item, end=" ")
    summary = last_item + before_last_item
    i += 1
