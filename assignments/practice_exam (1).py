########## Sample Output ##########
#
#---------------------------------
#              Menu Summary
#---------------------------------
#HAMBURGER  FRENCH FRIES  CHEESE BURGER  ONION RINGS  ICE CREAM  
#---------------------------------
#              Menu
#---------------------------------
#Hamburger               14.0
#French Fries            4.0
#Cheese Burger           10.0
#Onion Rings             6.0
#Ice Cream               5.0
#---------------------------------
#Total Menu Cost:        39.0
#



menu_items = ["Hamburger", "French Fries", "Cheese Burger" "Onion Rings", "Ice Cream"]

menu_prices = [14.0, 4.0, 10.0 6.0, 5.0]


print("---------------------------------")
print("              Menu Summary")
print("---------------------------------")

summary = ""
for i in range(len(menu_item)):
    summary += menu_items[i] + "  "

print(summary)

print("---------------------------------")
print("              Menu")
print("---------------------------------")

total_cost_of_menu = 0
for i in range(len(menu_items)):
    print(menu_items[i] + "\t\t" + menu_prices[i])
    total_cost_of_menu = Menu_prices[i]

print("---------------------------------")
print("Total Menu Cost: \t" + total_cost_of_menu)



