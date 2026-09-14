from products import products

name = input("what is your name ?")
print("hi", name)



print("Product List")
for product, price in products.items():
    print(product, ":", price, ("$"))


product_name = input("Enter the product name:")
if product_name in products:
    quantity = int(input("How many do you want? "))
    total = products[product_name] * quantity
    print("total Price:", total)
else:
    print("Product not found")
