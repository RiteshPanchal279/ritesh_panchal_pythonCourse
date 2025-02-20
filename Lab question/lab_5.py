# question 1
# Accept a name from the user and display that in lower case using lower() function

def toLower(name):
   lowertext=name.lower()
   print(lowertext)

name=input("Enter your name in capital: ")
toLower(name)

# question 2
# Write a function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. 

def numberTest(num):
   if(num==0):
      print("number is zero")
   elif(num < 0):
      print("Numbr is Negative")
   else:
      print("Numbr is Positive")

num = int(input("Entr the number : "))
numberTest(num)