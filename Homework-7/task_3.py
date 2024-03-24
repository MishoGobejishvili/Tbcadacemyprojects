import sys

# დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 10000 და დაბეჭდავს ამ რიცხვის
# შებრუნებულ მნიშვნელობას და ამ რიცხვში შემავალი ციფრების ჯამს. გამოიყენეთ while ციკლი

number = int(input("Enter number: "))
number_in_str = str(number)
reversed_number_str = ""
number_sum = 0
i = len(number_in_str)

if not (0 < number <= 10000):
    print("Invalid input")
    sys.exit(1)

while i > 0:
    number_sum += int(number_in_str[i - 1])
    reversed_number_str += number_in_str[i - 1]
    i -= 1

print("Reversed number is", reversed_number_str)
print("Reversed number in int is", int(reversed_number_str))  # in cases when numbers start with 0
print("Sum of digits:", number_sum)
