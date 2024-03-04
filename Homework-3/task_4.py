from forex_python.bitcoin import BtcConverter
import datetime

# დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს, როცა მომხმარებელმა იყიდა ბიტკოინი, ასევე მიიღებს დოლარში თანხას,
# რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად და ეკრანზე გამოიტანს დოლარში თანხას რომელიც მოიგო ან დაკარგა
# დღევანდელი ფასის გათვალისწინებით.

year_of_purchase = int(input("Could you please provide the specific year when you purchased your Bitcoin: "))
month_of_purchase = int(input("Could you please provide the specific month when you purchased your Bitcoin: "))
day_of_purchase = int(input("Could you please provide the specific day when you purchased your Bitcoin: "))
usd_paid_in_bitcoin = int(input("Could you please tell me how much you paid in USD for your Bitcoin?: "))
purchase_date = datetime.datetime(year_of_purchase, month_of_purchase, day_of_purchase)

converter = BtcConverter()
previous_btc = converter.convert_to_btc_on(usd_paid_in_bitcoin, 'USD', purchase_date)
up_to_date_btc = converter.convert_to_btc(usd_paid_in_bitcoin, 'USD')
print(previous_btc - up_to_date_btc)

if previous_btc > up_to_date_btc:
    print(f"You are in profit of {converter.convert_btc_to_cur(previous_btc - up_to_date_btc, 'USD')} USD")
elif previous_btc < up_to_date_btc:
    print(f"You are in loss of {converter.convert_btc_to_cur(up_to_date_btc - previous_btc, 'USD')} USD")
else:
    print("There is no profit or loss")

