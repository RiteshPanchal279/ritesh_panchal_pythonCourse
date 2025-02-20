# question 1
# Python program to check if the given string is a palindrome 

def plaindromeStr(str):
   revStr = ""
   for char in str:
      revStr=char+revStr
   if(str==revStr):
      print("String is plaindrome")
   else:
      print("String is not plaindrome")


str = input("Enter string: ")
plaindromeStr(str)


# question 2
# Python program to check if a given number is an Armstrong number

def armstrong(num):
    result=0
    while num>0:
      last=num%10
      result+=last**3
      num//=10
    return result

num = int((input("Enter number ")))
ans= armstrong(num)
if(ans == num ):
   print("Number is Armstrong ")
else:
   print("Number is not Armstrong ")