# 2. დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს. Პროგრამამ უნდა შეამოწმოს არის თუ არა შესაძლებელი
# ერთი სტრიქოქნის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.

user_input_one = input("Input:\n")
user_input_two = input("")
output = "Yes"

for c in user_input_two:
    if user_input_one.find(c) == -1:
        output = "No"
    else:
        user_input_one = user_input_one.replace(c, "", 1)

print("Output:", output)
