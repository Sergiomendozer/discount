# prompts user to enter original price
price = int(input("Enter the price:"))
# prompts user to enter percentage discount
discount = int(input("Enter discount percentage:"))
# inputs taken in and calculations are made below to get ne price
discount = discount / 100
dollars_off = price * discount
new_price = price - dollars_off
dollars_off = str(dollars_off)
new_price = str(new_price)
# informs user of the new price and the difference between original price and new price
print(
    "The new price is $"
    + new_price
    + ", it is $"
    + dollars_off
    + " off original price."
)
