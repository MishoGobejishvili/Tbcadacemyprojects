import sys

# 2. დაწერეთ პროგრამა რომელიც მიიღებს დადებით მთელ რიცხვს - n. 0 < n <= 1000.
# პროგრამამ უნდა დაბეჭდოს რიცხვების მიმდევრობა რომელიც მიიღება შემდეგი პირობით:
# თუ რიცხვი ლუწია, ეს რიცხვი უნდა გავყოთ 2-ზე, ხოლო თუ რიცხვი კენტია ეს რიცხვი უნდა გავამრავლოთ 3-ზე
# და დავუმატოთ 1, იქამდე სანამ არ მივიღებთ 1-ს.

n = int(input("Enter number: "))

if not (0 < n <= 1000):
    print("Invalid input")
    sys.exit(1)

while n != 1:
    print(int(n), end=" -> ")
    if n % 2 == 0:
        n /= 2
    else:
        n = (n * 3) + 1
print(1)
