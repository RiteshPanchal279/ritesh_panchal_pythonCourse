# 1: Scenario:
#  You are tasked with developing a hospital management system that handles different types of hospital staff: 
# Doctors, Nurses, and Administrative Staff. Each
# type of staff member has basic details such as name, ID, and department. Doctors have
# specializations, nurses have shifts, and administrative staff have roles. The system
# should allow you to display staff information and also calculate their monthly salaries
# based on their unique attributes.


class Staff:
   def __init__(self,name, id, department):
      self.name=name
      self.staff_id=id
      self.department=department

   def display_info(self):
      return f"Staff name is {self.name} and it is from {self.department}"
   
class Doctor(Staff):
   def specializations_info(self,special):
      return f"Doctor {self.name} is specializations in {special}"
   def salary_info(self,salary,insentive):
      return salary+insentive
   
   def display_info(self):
      return f"Doctor name is {self.name} and salary is {self.salary_info(20000,4000)} for {self.department}  department"
   
class Nurse(Staff):
   def shift_info(self,shift):
      return f"nurse name is{self.name} and shift is {shift}"
   
   def salary_info(self,salary,bonous):
      return salary+bonous

   def display_info(self):
      return f"Nurse name is {self.name} and salary is {self.salary_info(10000,5000)} for {self.department}  department"
   

class AdminStaff(Staff):
    def role_set(self,role):
      self.role = role
    
    def display_info(self):
        return f"Administrative staff name {self.name} and role is {self.role} for {self.department}  department "

doc=Doctor("Dr.Son",101,"Cardiology")
print(doc.specializations_info("Cardiologist"))
print(doc.display_info())

nur=Nurse("nurse jane",100,"Pediatrics")
print(nur.shift_info("Night"))
print(nur.display_info())

adm=AdminStaff("John Doe", 303, "HR")
adm.role_set("Manager")
print(adm.display_info())



# 2. : Vehicle Rental System
# Imagine you are developing a Vehicle Rental System where different types of vehicles
# (like Car, Bike, and Truck) are available for rent.
# ● All vehicles have some common attributes like registration_number, brand, and
# rental_price_per_day.
# ● Each type of vehicle has a different pricing strategy. For example, trucks hav
# additional charges for heavy loads, and cars have insurance fees included.
# Task:
# ● Design a class Vehicle with a method calculate_rental_cost(), which will be
# overridden in the subclasses Car, Bike, and Truck.
# ● Use method overriding to customize the rental cost calculation for each vehicle
# type.
# ● Use the super() method to access common attributes from the Vehicle class.


class Vehicle:
    def __init__(self, registration_number, brand, rental_price_per_day):
        self.registration_number = registration_number
        self.brand = brand
        self.rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days

    def display_info(self):
        return f"Vehicle: {self.brand}, Reg No: {self.registration_number}, Base Price per Day: ${self.rental_price_per_day}" 

class Car(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, insurance_fee):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.insurance_fee = insurance_fee

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) + (self.insurance_fee * days)

    def display_info(self):
        return super().display_info() + f", Insurance Fee per Day: ${self.insurance_fee}"

class Bike(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day):
        super().__init__(registration_number, brand, rental_price_per_day)

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)  # No extra charges for bikes

class Truck(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, heavy_load_fee):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.heavy_load_fee = heavy_load_fee

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days) + self.heavy_load_fee

    def display_info(self):
        return super().display_info() + f", Heavy Load Fee: ${self.heavy_load_fee}"

# Example Usage:
car = Car("ABC123", "Toyota", 50, 10)
bike = Bike("XYZ789", "Honda", 20)
truck = Truck("TRK456", "Volvo", 100, 50)

print(car.display_info())
print(f"Total Cost for 3 days: ${car.calculate_rental_cost(3)}")
print(bike.display_info())
print(f"Total Cost for 3 days: ${bike.calculate_rental_cost(3)}")
print(truck.display_info())
print(f"Total Cost for 3 days: ${truck.calculate_rental_cost(3)}")










