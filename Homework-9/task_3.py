from datetime import datetime
# 3. დაწერეთ პროგრამა რომელიც მიიღებს თარიღს.
# Პროგრამამ თარიღი უნდა გადაიყვანოს განსხვავებულ ფორმატში და დაბეჭდოს ეკრანზე.
# Შემომავალი და გამომავალი თარიღების ფორმატები იხილეთ მაგალითებში. Შემომავალი სტრიქონის ფორმატის განმარტება:

input_date = input("Input: ")
sign = ''
hour = input_date[input_date.find('T') + 1:input_date.find('T') + 3]
timezone = input_date[input_date.find('.'):]
input_format_date = "%Y-%m-%dT%H:%M:%S.%f%z"
output_format_date = "%d-%m-%Y '%M:%S"
formatted_date = datetime.strptime(input_date[:], input_format_date).strftime(output_format_date)

if input_date.find('T') != -1 and int(hour) > 12:
    hour = str(int(hour) - 12)
hour += ":"

if timezone.find('+') != -1:
    sign = '+'
    timezone = timezone[timezone.find('+') + 2:timezone.find('+') + 3]
elif timezone.find('-') != -1:
    sign = '-'
    timezone = timezone[timezone.find('-') + 2:timezone.find('-') + 3]
else:
    timezone = ""
formatted_date = formatted_date.replace("'", hour) + " " + sign + timezone
print(formatted_date)
