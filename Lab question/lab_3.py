# question 1

print("press 1 Household pourpose: rate per unit : 2rs")
print("press 2 small business pourpose: rate per unit : 5rs")
print("press 3 industrial pourpose: rate per unit : 10rs")
user_type=input("Enter number : ")
user_consume_unit=int(input("Enter month unit consumption: "))

if(user_type=="1" ):
   print("your bill is : ",2*user_consume_unit)
elif(user_type=="2" ):
   print("your bill is : ",5*user_consume_unit)
elif(user_type=="3"):
   print("your bill is : ",10*user_consume_unit)
else:
   print("Invalid input")

# question 2

user_travel=int(input("Enter KM that you travel: "))
if(user_travel <=10):
   print("Your charge is  :",user_travel*10)
elif(user_travel>11 and user_travel<=20):
   print("Your charge is  :",user_travel*5)
else:
   print("Your charge is  :",user_travel*4)