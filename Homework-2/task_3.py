
# Დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს. Პროგრამამ უნდა დაბეჭდოს ყველა ყველა მარტივი გამყოფი ერთ ხაზზე. Შემოსული რიცხვის მაქსიმალური მნიშვნელობა უნდა იყოს 10. Მაგალითი: თუ პროგრამას გადავეცით 6,
# გამოსავალზე უნდა დაიბეჭდოს 2, 3. ახსნა: 6 იყოფა 2-ზეც და 3-ზეც. 2 და 3 არის მარტივი რიცხვები. Დაიცავით პროგრამა ისეთი არგუმენტებისგან, რომლებიც არ არის დასაშვები.

input_number = int(input("Enter number up to 10: "))

if input_number > 10:
    print("Number is more than 10 ")
elif 10 >= input_number > 0:
    if input_number % 2 == 0:
        print("2, ", end="")
    if input_number % 3 == 0:
        print("3, ", end="")
    if input_number % 4 == 0:
        print("4, ", end="")
    if input_number % 5 == 0:
        print("5, ", end="")
elif input_number < 0:
    print("Number is less than zero")
