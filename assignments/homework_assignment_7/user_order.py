#Fu An Yang
#1051888
#assignment#7
#4/12
KFC={"burger":10,"fries":1,"ice_cream":2,"fry_chicken":7,"egg_tart":5}
order_cost=[]
food =KFC.keys()
process_active = True
while process_active:
    order=input("enter an item")
    if order=="N" :
        process_active=False
    elif order in food:
        print(order.title()+": $"+str(KFC[order]))
        order_cost.append(KFC[order])
    else:
        print("We do not have "+order.title())

print("-----------------------------")
print("Order Total: $"+ str(sum(order_cost))
