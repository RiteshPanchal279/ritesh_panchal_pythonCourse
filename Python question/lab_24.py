# 1: Employee Salary Management (Abstraction) You are tasked with building an employee salary management system.Use abstraction to create a base class Employee and two subclasses, FullTimeEmployee and PartTimeEmployee.
#  ● Abstract Class: Employee with abstract methods calculate_salary() and get_employee_details(). 
# ● FullTimeEmployee: Overrides calculate_salary() by considering a monthly fixed salary.
# ● PartTimeEmployee: Overrides calculate_salary() by considering an hourly rate and hours worked. 

# Task: 1. Create the abstract class and its subclasses. 
# 2. Implement the salary calculation for both types of employees.
#  3. Instantiate both employee types, calculate salaries, and display their details.
#  4. Add an abstract method raise_salary() that forces both subclasses to implement their logic for raising the salary. 

from abc import ABC, abstractmethod

class Employee(ABC):

   def __init__(self, name, employee_id):
      self.name = name
      self.employee_id = employee_id

   @abstractmethod
   def calculate_salary(self):
      pass

   @abstractmethod
   def get_employee_details(self):
      pass

   @abstractmethod
   def raise_salary(self,percentage):
      pass



class FullTimeEmployee(Employee) :

   def __init__(self,name,employee_id,monthly_salary):
      super().__init__(name,employee_id)
      self.monthly_salary=monthly_salary
      

   def calculate_salary(self):
      return self.monthly_salary
   
   def get_employee_details(self):
      return f"Full-Time Employee: {self.name}, ID: {self.employee_id}, Salary: {self.calculate_salary()}rs"

   def raise_salary(self, percentage):
      self.monthly_salary += self.monthly_salary * (percentage / 100)


class PartTimeEmployee(Employee):
   def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

   def calculate_salary(self):
      return self.hourly_rate * self.hours_worked
    
   def get_employee_details(self):
      return f"Part-Time Employee: {self.name}, ID: {self.employee_id}, Salary: {self.calculate_salary()}rs"
    
   def raise_salary(self, percentage):
      self.hourly_rate += self.hourly_rate * (percentage / 100)




full_time_emp = FullTimeEmployee("Dhoni ", 101, 50000)
part_time_emp = PartTimeEmployee("Rohit", 102, 200, 40)

# Display details before salary raise
print(full_time_emp.get_employee_details())
print(part_time_emp.get_employee_details())

# Raise salary
full_time_emp.raise_salary(10)  # 10% raise
part_time_emp.raise_salary(5)   # 5% raise

# Display details after salary raise
print("\nAfter Salary Raise:")
print(full_time_emp.get_employee_details())
print(part_time_emp.get_employee_details())




# 2: Smart Home Devices (Encapsulation and Property Decorators) Develop a system to manage smart home devices.
#  Implement a class SmartDevice that: 
# ● Uses encapsulation to store the device’s status (__is_on, default to False).
#  ● Has a turn_on() and turn_off() method to change the device status.
#  ● Uses a property decorator to expose the device’s status as a property (is_on) with a setter to prevent turning it on if certain conditions (like low battery) are met. 

# Task: 1. Implement the SmartDevice class. 
# 2. Simulate turning the device on and off while managing conditions like low battery.
# 3. Use the property method to ensure users cannot turn on the device when the battery is below a threshold.


class SmartDevice:
    def __init__(self, name, battery_level=100):
        self.name = name
        self.__is_on = False  # Encapsulated attribute
        self.__battery_level = battery_level

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, value):
        if self.__battery_level < 20 and value:  # Prevent turning on if battery < 20%
            print(f"Cannot turn on {self.name}. Battery too low!")
        else:
            self.__is_on = value
            state = "ON" if value else "OFF"
            print(f"{self.name} is now {state}.")

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def charge_battery(self, amount):
        self.__battery_level = min(100, self.__battery_level + amount)
        print(f"{self.name} charged to {self.__battery_level}% battery.")

    def drain_battery(self, amount):
        self.__battery_level = max(0, self.__battery_level - amount)
        print(f"{self.name} battery drained to {self.__battery_level}%.")

# Simulate smart device usage
device = SmartDevice("Smart Light", battery_level=25)
device.turn_on()  
device.drain_battery(10)  
device.turn_on()  

device.charge_battery(10) 

device.turn_on()  
device.turn_off()

