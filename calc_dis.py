price=float(input("Enter the price of the product: "))
discount=float(input("Enter the discount percentage: "))
final_price=lambda price,discount: price-(price*discount/100)
print("The final price after discount is:",final_price(price,discount))