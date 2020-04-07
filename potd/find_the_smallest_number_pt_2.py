list_of_numbers=[23,30,1,23,45,8,3,52]

i=0
current=list_of_numbers[0]
while i< len(list_of_numbers)-1:
    next_number=list_of_numbers[i+1]
    if next_number<current :
        current=next_number
    i=i+1
print(current)


