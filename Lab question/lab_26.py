# 1 Imagine you are developing a personal finance tracking application. Create a custom module named finance.py that includes functions for calculating expenses, income, and savings. Describe the functions you would include and how you would import this module in your main application

from finance import *

if __name__ =="__main__":
   expenses = [1500,400,100]
   income=[4000,1200]

   total_expenses = calculate_expenses(expenses)
   total_income = calculate_income(income)
   total_savings = calculate_savings(total_income,total_expenses)

   print(f"Total Expenses: ${total_expenses}")
   print(f"Total Income: ${total_income}")
   print(f"Total Savings: ${total_savings}")


# 2: ● Import the random module as rnd and generate a random integer between 1 and 100. ● Import the math module and calculate the square root of 49 and the sine of 90 degrees (convert degrees to radians using math.radians).

import random as rnd 
import math

# Generate a random integer between 1 and 100
random_number = rnd.randint(1,100)
print(f"Rnadom number:{random_number}")

# Calculate the square root of 49
sqrt_49 = math.sqrt(49)
print(f"Square root of 49: {sqrt_49}")

# Calculate the sine of 90 degrees
sine_90 = math.sin(math.radians(90))
print(f"Sine of 90 degrees: {sine_90}")