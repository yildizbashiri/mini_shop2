import os
from dotenv import load_dotenv
from products import products


load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")
open_admin = input("do u want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password  :") 
    if entered_password == admin_password:
        print("admin! hi")
    else:
        print("wrong password")


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
    file = open("sales.txt", "a")
    file.write(f"{name} : {product_name} : {quantity} : {total}\n")
    file.close()
else:
    print("Product not found")
