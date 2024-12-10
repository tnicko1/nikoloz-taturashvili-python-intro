"""
Write a program that reads sales information from the file with the structure described in the previous task.

a. The program should find the customer who made the maximum purchase (by the number of products in one purchase), if there are several, then a list of customers.

b. The program should find the customer who made the maximum purchase (by the total value of all purchases), if there are several, then a list of customers.

c. The program should find the arithmetic mean of the purchase value

d. The program should find the arithmetic mean of the quantities of orders

e. The program should find the product sold in the largest quantity, if there are several, then a list of products.

Collect the found data in a dict type object and write it to the stats.json file. Format the stats.json file so that the data is presented in an easily readable form.
"""


import json

file = open("../task_1/data.txt", "r")
file_data = file.read()
file.close()

max_spent = 0
max_users = []
user_spending = {}
max_spent_all_products = 0
max_users_all_products = ""
average_price = 0
average_amount = 0
most_sold_product = []
product_sales = {}

for line in file_data.split('\n')[1:]:
    properties = line.split(',')
    user = properties[0]
    product = properties[1]
    amount = int(properties[2])
    price = float(properties[3])
    total_spent = amount * price
    average_price += price
    average_amount += amount

    if user in user_spending:
        user_spending[user] += total_spent
    else:
        user_spending[user] = total_spent

    if user_spending[user] > max_spent:
        max_spent_all_products = user_spending[user]
        max_users_all_products = [user]
    elif user_spending[user] == max_spent_all_products:
        max_users_all_products.append(user)

    if total_spent > max_spent:
        max_spent = total_spent
        max_users = [user]
    elif total_spent == max_spent:
        max_users.append(user)

    if product in product_sales:
        product_sales[product] += amount
    else:
        product_sales[product] = amount

average_price /= len(file_data.split('\n')[1:])
average_amount /= len(file_data.split('\n')[1:])

max_sold_amount = max(product_sales.values())
most_sold_product = [product for product, amount in product_sales.items() if amount == max_sold_amount]

print(f"The user(s) who spent the most on a single product is {', '.join(max_users)} with a total of ${max_spent} spent.")
print(f"The user(s) who spent the most on all products is {', '.join(max_users_all_products)} with a total of ${max_spent_all_products} spent.")
print(f"The average amount spent on a product is ${average_price}.")
print(f"The average amount of products bought is {average_amount}.")
print(f"The most sold product(s) is {', '.join(most_sold_product)} with a total of {max_sold_amount} products sold.")

stats = {
    "max_spent_single_product": {
        "users": max_users,
        "amount": max_spent
    },
    "max_spent_all_products": {
        "users": max_users_all_products,
        "amount": max_spent_all_products
    },
    "average_price": average_price,
    "average_amount": average_amount,
    "most_sold_product": {
        "products": most_sold_product,
        "amount": max_sold_amount
    }
}

with open("stats.json", "w") as stats_file:
    json.dump(stats, stats_file, indent=4)