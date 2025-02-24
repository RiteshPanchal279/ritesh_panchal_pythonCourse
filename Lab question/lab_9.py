# 1. Write a Python program to get the largest and smallest number from a list without built-in functions. 

myList=[3,5,7,1,55,6]
max=myList[0]
min=myList[0]
for i in myList:
   if(i>max):
      max=i

for i in myList:
   if(i<min):
      min=i

print("Largest number is: ",max)
print("Smallest number is: ",min)

# 2. Write a Python program to find duplicate values from a list and display those.

a = [1, 2, 3, 4, 5, 2, 6, 3,1]

# A set to keep track of elements that have been seen
seen = set()
# A list to store duplicates found in the input list
duplicates = []

# Iterate over each element in the list
for i in a:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)