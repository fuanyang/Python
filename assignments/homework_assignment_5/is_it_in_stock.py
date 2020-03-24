#Fu An Yang
#1051888
#Assignment#5
#3/29

menu_items_in_stock=["Tacos","Chips","Salsa","Quesadilla"]
Customer_order=["Tacos","Gucamole","Burrito","Chips","Salsa"]
new_menu=[menu.lower() for menu in menu_items_in_stock]
new_customer=[customer.lower() for customer in Customer_order]
print(new_menu)
print(new_customer)
for order in Customer_order:
    if order in menu_items_in_stock:
        print("We have "+order+" in stock.")
    else:
        print("We do not have "+order+" in stock.")