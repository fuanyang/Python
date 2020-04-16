#Fu An Yang
#1051888
#Assignment#8
#4/19

def ask_user_for_menu_item_name():
    item_name=input("please enter an item:")
    return item_name
    

def ask_user_for_menu_item_cost():
    cost=input("please enter the cost:")
    return cost

def add_menu_item(menu,item_name,cost):
    menu[item_name]=cost
    return menu

menu={}
process_active=True
while process_active:
    
    item_name=ask_user_for_menu_item_name()
    if item_name in menu:
        print("the item is already exit")
        
    cost=ask_user_for_menu_item_cost()
    
    add_menu_item(menu,item_name,cost)
    repeat=input("Do you want to continue? y/n")
    if repeat=="n":
            process_active=False
print("----------------menu---------------")
for k,v in menu.items():
    print(menu)