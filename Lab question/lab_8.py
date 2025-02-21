# question 1
#  WAP to print count of uppercase, lowercase, numbers and special characters in a string.

str="This is My Lab Question and Lab No is 8"
upr,lwr,num, spl=0,0,0,0

for i in range(len(str)):
    if str[i]>='A' and str[i]<='Z':
        upr+=1
    elif str[i]>='a' and str[i]<='z':
        lwr+=1
    elif str[i]>='0' and str[i]<='9':
        num+=1
    else:
        spl+=1


print("Uppercase letters : ",upr)
print("Lowercase letters : ",lwr)
print("Numbers : ",num)
print("Special chacters ",spl)

# question 2
# WAP with several string methods.

ans=str.find('My') # this will return the index of string that we pass as paramater
# print(ans)

title=str.title()
# print(title) # this will capital first each word in string

table = str.maketrans("", "", "aeiou")  # Remove vowels
result = str.translate(table)
print(result)