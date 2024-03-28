# 3. პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო, პირველი და
# შუა ასოები 5-ჯერ while ლუპით. თუ შემოყვანილი ტექსტის ზომა არის
# ლუწი, მაშინ პროგრამამ უნდა დაბეჭდოს შუა ორი სიმბოლო

input_str = input("Enter text: ")
middle_index = int(len(input_str) / 2)

output_str = 5 * input_str[0] + " "

if len(input_str) % 2 == 0:
    output_str += 5 * (input_str[middle_index - 1] + input_str[middle_index]) + " "
else:
    output_str += 5 * input_str[middle_index] + " "

output_str += 5 * input_str[len(input_str) - 1] + " "

print(output_str)
