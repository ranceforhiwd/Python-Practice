import json

tax = 0.48

products = {
    "Jacket":34.23,
    "Hat":15.99,
    "Pencel":1.12,
    "Beer":1.75
}

for x in products:
    price = products[x]
    final_price = price + (price*tax)
    print(x, "Original Price:", products[x], "Final Price:", round(final_price, 2))