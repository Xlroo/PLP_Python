# <!-- Create a function named calculate_discount(price, discount_percent)
# that calculates the final price after applying a discount.
# The function should take the original price (price) and
# the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, 
# return the original price.
# Using the calculate_discount function,
# prompt the user to enter the original price of an item 
# and the discount percentage. Print the final price after applying the discount,
#  or if no discount was applied, print the original price. -->

def calculate_discount():
    price = int(input("What's the price of the item? "))
    discount_percent = int(input("What's the percentage discount of the item? "))
    final_price = 0
    if discount_percent < 20 :
        final_price = price
        print(f"The final price is {final_price}")
    elif discount_percent >= 20:
        final_price = (100 - discount_percent)/100 * price
        print(f"The final price is {final_price}")
    else:
        print("Invalid input, try again!")
calculate_discount()


 