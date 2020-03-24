#Fu An Yang
#1051888
#PotD#5
#3/29
odd_list=[]
list_of_numbers=[23,45,17,33,45,18,93,2]
for number in list_of_numbers:
    if number % 2 != 0:
        odd_list.append(number)
print(odd_list)
print(sum(odd_list))
