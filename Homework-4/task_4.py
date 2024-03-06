
# 4. * დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 20.
# Პროგრამამ უნდა იპოვოს მიმდევრობის n-ური წევრი. Მიმდევრობა განისაზღვრება შემდეგნაირად:
# ნულოვანი წევრი არის 0, პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი.
# Მაგალითად: Enter number: 4 3

number = int(input("Enter number: "))
last_item = 1
before_last_item = 0
summary = 0

if 0 <= number < 20:
    for i in range(number):
        summary = last_item + before_last_item
        if i % 2 == 0:
            last_item = summary
        else:
            before_last_item = summary
    print(summary)
else:
    print("Invalid input")
