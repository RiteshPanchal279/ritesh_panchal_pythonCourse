# 1: Create a program that greets the user based on the current time (e.g., "Good Morning" before noon, "Good Afternoon" in the afternoon, and "Good Evening" in the evening). Use the datetime module to retrieve the current time and conditionally display a greeting. Output:

from datetime import datetime

def greeting():
   current_date = datetime.now()
   current_hr = current_date.hour

   if current_hr<12:
      greet="Good Morning"
   elif 12 <= current_hr<18:
      greet = "Good Afternoon"
   else :
      greet = "Good Evening"

   print(f"{greet} !  The current time is : {current_date.strftime('%H:%M:%S')}")

greeting()


# 2: Write a Python program that asks the user to input two dates (in YYYY-MM-DD format) and calculates the number of days between the two dates. Use the datetime module to perform the calculation

def calc_day_between_two_date():

   f_date = input("Enter the first date (YYYY-MM-DD): ")
   s_date = input("Enter the second date (YYYY-MM-DD): ")

# strptime :- It converts a string representation of a date into a datetime object

#strftime:- It converts a datetime object into a formatted string.
   try:
      date1 = datetime.strptime(f_date,"%Y-%m-%d")
      date2 = datetime.strptime(s_date,"%Y-%m-%d")
      diff = abs(date2-date1)

      print(f"The number of days between {date1} and {date2} is {diff.days} days.")
   except ValueError:
      print("Invalid date format! Please use the format YYYY-MM-DD.")



calc_day_between_two_date()