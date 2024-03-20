# 4. *დაწერეთ პროგრამა რომელიც მომხმარებლის შემოყვანილ ტექსტს დაშიფრავს ან განშიფრავს და დაბეჭდავს ეკრანზე.

input_action = input("Enter action (e/d): ")
input_str = input("Enter text: ")
output_str = ""
keyboard_layout = "qwertyuiopasdfghjklzxcvbnm"

if input_action != "e" and input_action != "d":
    print("Incorrect action ")
    exit(1)
elif input_action == "e":
    for i in range(len(input_str)):
        for j in range(len(keyboard_layout)):
            if input_str[i] == keyboard_layout[j]:
                if j == 9:
                    output_str += keyboard_layout[0]
                elif j == 18:
                    output_str += keyboard_layout[10]
                elif j == 25:
                    output_str += keyboard_layout[19]
                else:
                    output_str += keyboard_layout[j + 1]
elif input_action == "d":
    for i in range(len(input_str)):
        for j in range(len(keyboard_layout)):
            if input_str[i] == keyboard_layout[j]:
                if j == 0:
                    output_str += keyboard_layout[9]
                elif j == 10:
                    output_str += keyboard_layout[18]
                elif j == 19:
                    output_str += keyboard_layout[25]
                else:
                    output_str += keyboard_layout[j - 1]
print(output_str)
