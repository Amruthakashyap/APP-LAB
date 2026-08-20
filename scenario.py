#An online store has a lost of products
# the system must
# add gst to every product
# consider only products above ₹500 after gst
# calculate the total using reduce function 


from functools import reduce
prices = list(map(float, input("Enter product prices: ").split()))
prices_with_gst = list(map(lambda x: x * 1.18, prices))
filtered_prices = list(filter(lambda x: x > 500, prices_with_gst))
total = reduce(lambda x, y: x + y, filtered_prices, 0)
print("Original Prices:", prices)
print("Prices with GST:", prices_with_gst)
print("Products above ₹500:", filtered_prices)
print("Total:", round(total, 2))