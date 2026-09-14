name = input("what is your name ?")
print("hi", name)

products = {
    "milk" : 30,
    "apple" : 20,
    "bread" : 10,
}

print("Product List")
for product, price in products.items():
    print(product, "-", price)

product_name = input("Enter the product name:")

total = 0
for product in product_name.split():
    if product in products:
        total = total + products[product]
print("total Price:", total)
