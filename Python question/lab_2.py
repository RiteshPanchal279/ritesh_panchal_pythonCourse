# 1. Using input function take two number and then swap the number

num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))
print("Number Before swap")
print("Num1: ",num1)
print("Num2: ",num2)

# swaping the number 
temp=num1
num1=num2
num2=temp
print("Number After swap")
print("Num1: ",num1)
print("Num2: ",num2)

# Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

amount=200
year=5
interest=5

simple_intrest = 200 * 5 * 5 / 100
print("The intrest is",simple_intrest)