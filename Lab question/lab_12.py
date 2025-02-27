# 1. Write a Python program to Get Only unique items from two sets. 
# Output: {70, 40, 10, 50, 20, 60, 30} 

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 

result1 = set1.union(set2)
print("The Result is : ",result1)

# 2. Write a Python program to Return a set of elements present in Set A or B, but not both. 
# Output: {20, 70, 10, 60}

setA = {10, 20, 30, 40, 50} 
setB = {30, 40, 50, 60, 70} 

result2= setA.symmetric_difference(setB)
print("The Result is : ",result2)
