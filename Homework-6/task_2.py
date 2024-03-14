
# 2. ლექციაზე განხილული პაროლის შემოყვანის ამოცანა გადაჭერით for ციკლის გამოყენებით

password = "intro_to_python"
amount_of_tries = 3
print("Enter password: ", end="")

for i in range(0, amount_of_tries):
    user_input = input()
    if user_input == password:
        print("Welcome back")
        break
    elif user_input != password and i != amount_of_tries - 1:
        print("Try again: ", end="")
