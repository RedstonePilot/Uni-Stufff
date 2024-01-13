"""A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage andpackaging. 
If an order is over £50.00, the P&P is reduced by £1.50. 
Write a function that willtake the number of kilo of bananas and return the cost of the order in pence. 
Then write ascript requesting the user to input the number of kilos for an order and print the cost of 
that order"""

def cost(kilos):
    price = 3.00 * float(kilos)
    if price > 50:
        return f"{int((price + 3.49))*100} pence"
    return f"{int((price + 4.99)*100)} pence"
weight_banana = input("Enter the weight of the bananans: ")
print(cost(weight_banana))