#Write your code here.
def calculate_vat(price, vat):
    try:
        price = float(price)
        vat = float(vat)
        total_price = price + price * (vat / 100)
        return round(total_price)
    except ValueError:
        return "Invalid Input"

price = input()
vat = input()

print(calculate_vat(price, vat))
