# 1. პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა. დაბეჭდოს შეყვანილი სტრიქონის
# ყველა ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი.

input_str = input("Enter text: ")

for i in range(len(input_str)):
    if i % 2 == 0 and input_str[i] != 'e':
        print(input_str[i], end="")
