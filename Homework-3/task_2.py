from datetime import datetime

# 2. დაწერეთ პროგრამა რომელიც მიიღებს 3 მნიშვნელობას: რომელ წელსაა დაბადებული ადამიანი,
# მერამდენე თვეშია დაბადებული და რა რიცხვშია დაბადებული.
# Შემდეგ კი ეკრანზე გამოიტანს კვირის რომელ დღესაა დაბადებული ადამიანი. იხ module datetime

year_of_birth = int(input("Enter year of birth: "))
month_of_birth = int(input("Enter month of birth: "))
day_of_birth = int(input("Enter day of birth: "))
date_of_birth = datetime(year_of_birth, month_of_birth, day_of_birth)

print("You were born on", datetime.strftime(date_of_birth, "%A"))

