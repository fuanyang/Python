#Fu An Yang
#1051888
#assignment#6
#4/4
KFC={"burger":10,"fries":1,"ice_cream":2,"fry_chicken":7,"egg_tart":5}
orders=["ice_cream", "egg_tart","fries","donut","taco"]
order_cost=[]
food =KFC.keys()
for order in orders:
        if order in food:
            print(order.title()+": $"+str(KFC[order]))
            order_cost.append(KFC[order])
        else:
            print("We do not have "+order.title())
print("-----------------------------")
print("Order Total: $"+ str(sum(order_cost)))
    