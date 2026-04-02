rates = {

"USD": 1.

"INR": 83.

"EUR": 0.92,

"GBP": 0.78

amount = float(input("Enter amount: "))

from_currency = input("From Currency (USD/INR/EUR/GBP): ").upper()

to_currency = input("To Currency (USD/INR/EUR/GBP): ").upper()

if from_currency not in rates or to_currency not in rates:

print("Invalid currency")

else:

#Convert to USD first, then to target

usd_amount = amount / rates[from_currency]

result = usd_amount * rates[to_currency] print("Converted Amount:", round(result, 2))
