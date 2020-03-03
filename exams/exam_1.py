###################################
#             Exam 1
###################################
# Name Fu An Yang
# StudentId 1051888
# Date 3/2/2020

###################################
#             Sample Output
###################################


# ---------------------------------
#             Grocery List
# ---------------------------------
# Apples
# Spinach
# Eggs
# Chicken
# Green Beans
# Potatoes
# ---------------------------------
#               Receipt
# ---------------------------------
# $2.99: APPLES
# $3.99: SPINACH
# $4.99: EGGS
# $4.49: CHICKEN
# $1.99: GREEN BEANS
# $3.49: POTATOES
# ---------------------------------
# Total:
# $21.94

###################################

grocery_list = ["apples", "spinach", "eggs", "chicken", "green beans", "potatoes"]

grocery_item_price = [2.99, 3.99, 4.99, 4.49, 1.99, 3.49]


print("---------------------------------")
print("            Grocery List")
print("---------------------------------")

for i in range(len(grocery_list)):
    print(grocery_list[i].title())


print("---------------------------------")
print("              Receipt")
print("---------------------------------")

grocery_bill_total = 0
for i in range(len(grocery_list)):
    print("$" + str(grocery_item_price[i]) + ": " + grocery_list[i].upper())
grocery_bill_total =sum(grocery_item_price)

print("---------------------------------")
print("Total:")
print("${0:.2f}".format(grocery_bill_total))


