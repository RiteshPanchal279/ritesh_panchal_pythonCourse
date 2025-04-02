# 1.Write a Python program to get the key, value and item in a dictionary.

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for key,value in dict_num.items():
   print("key:",key," value: ",value)

# 2. Write a Python program to deduce use of multiple dictionary functions.

dict_new={"one":22,"two":33,"three":9,"four":66,"five":54,"six":90}

print(dict_new)
dict_new.update({"seven":12}) # add new item
print(dict_new)

del dict_new["one"] # delete the one key and it's value

pop_value=dict_new.pop("two") # Will remove two and return its value
print(pop_value)

copy_dict = dict_new.copy() # copy the dictionary
print(copy_dict)

copy_dict.clear() # will clear the dictionary
print(copy_dict)