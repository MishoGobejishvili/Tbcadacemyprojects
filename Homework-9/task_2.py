# 2. დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს. Პროგრამამ უნდა შეამოწმოს არის თუ არა შესაძლებელი
# ერთი სტრიქოქნის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.

user_input_one = input("Input:\n")
user_input_two = input("")
text_one = user_input_one
text_two = user_input_two
output = "Yes"

if len(user_input_two) > len(user_input_one):
    text_one = user_input_two
    text_two = user_input_one

for c in text_one:
    if text_two.find(c) == -1:
        output = "No"
    else:
        text_two = text_two.replace(c, "", 1)

print("Output:", output)
