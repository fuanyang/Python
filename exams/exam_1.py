###################################
#             Exam 1
###################################
# Name
# StudentId
# Date

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

grocery_list = ["apples", "spinach", "eggs", "chicken" "green beans", "potatoes"]

grocery_item_price = [2.99, 3.99 4.99, 4.49, 1.99, 3.49]


print("---------------------------------")
print("            Grocery List")
print("---------------------------------")

for i in range(len(grocery_lst)):
    print(grocery_list[i])


print("---------------------------------")
print("              Receipt")
print("---------------------------------")

grocery_bll_total = 0
for i in range(len(grocery_list)):
    print("$" + grocery_item_price[i] + ": " + grocery_list[1].upper())
    grocery_bill_total = grocery_item_price[i]

print("---------------------------------")
print("Total:")
print("${0:.2f}".format(grocery_bill_total))
