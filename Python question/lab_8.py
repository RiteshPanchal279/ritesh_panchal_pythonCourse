# question 1
# WAP to remove repeated members from a string.print original and resultant string.

input_string = "this is is this more and more repeated string "
result_str=""

print("Original String :",input_string)

for char in input_string.split(' '):
    if char not in result_str:
        result_str+=' '+char

print("string as duplicate removed :",result_str)

# question 2
# WAP deducing multiple string methods.

str = "My new string Hello, world!"

print(str.find("world"))   # 21 (index of first occurrence)
print(str.index("new"))  # 3 (like find, but raises an error if not found)
print(str.count("o"))      # 2 (number of times 'o' appears)
print(str.startswith("Hello"))  # false
print(str.endswith("!"))    # True
print(str.replace("world","python")) #"My new string Hello, python!"