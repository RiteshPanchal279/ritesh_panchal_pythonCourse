# 1. WAP to create a tuple and append another tuple to it get the count of total members & repeated members similarly print length of this new tuple

tup_one=(3,4,5,6,8,7,7,3)
tup_two=(6,5,2,8,3,2,3)
print("********* Question 1 ***********")

new_add_tup=tup_one+tup_two
print(new_add_tup) # add two tuple

print(len(new_add_tup)) # count of total member

print(new_add_tup.count(3)) # print the count of reapeted member



# 2. WAP to to deduce use of sorting in tuples.
print("********* Question 2 ***********")
tup_for_sort=(5,3,8,1,9,4,6)

print("Before sorted: ",tup_for_sort)
sorted_ans = tuple(sorted(tup_for_sort)) # sorted tuple

print("After sorted: ",sorted_ans)

   

   