# Q.1 --> Create a class Employee that manages employee details:
#  1. Instance Attributes:  name: The employee's name.  salary: The employee's salary.  position: The employee's position. 
# 2. Methods:  promote(self, new_position): Updates the employee's position. update_salary(self, new_salary): Updates the employee's salary. display_info(self): Displays the employee's name, position, and salary

class Employee:
   def __init__(self,name,salary,position):
      self.name=name
      self.salary=salary
      self.position=position

   def promote(self, new_position):
      self.position=new_position
      print(f"{self.name} has been promoted to {self.position}.")
   
   def update_salary(self, new_salary):
      self.salary=new_salary
      print(f"{self.name}'s salary has been updated to ${self.salary}.")

   def display_info(self):
      print(f"Employee Name: {self.name}")
      print(f"Position: {self.position}")
      print(f"Salary: ${self.salary}")


emp1 = Employee("Ritesh", 50000, "Software Engineer")
emp1.display_info()
emp1.promote("Senior Software Engineer")
emp1.update_salary(70000)
emp1.display_info()


# Q.2-->
# Create a class MovieLibrary that manages a collection of movies:
# 1. Class Attribute: ○ available_movies: A list of all movies available in the library. 
# 2. Instance Attributes: ○ member_name: The name of the library member. ○ borrowed_movies: A list of movies borrowed by the member. 
# 3. Methods: ○ borrow_movie(self, movie): Borrows a movie from the library if available. ○ return_movie(self, movie): Returns a movie to the library. ○ view_borrowed_movies(self): Prints a list of movies borrowed by the member

class MovieLibrary:
   available_movies=["Dhoom","3 Idiots","Sholay","Bahubali","Lagaan","PK","Drishyam","Rockstar"]

   def __init__(self,name):
      self.name=name
      self.borrowed_movies=[]

   def borrow_movie(self, movie):
      if movie in MovieLibrary.available_movies:
         MovieLibrary.available_movies.remove(movie)
         self.borrowed_movies.append(movie)
         print(f"{self.name} borrowed {movie}")
      else:
         print(f"Sorry, '{movie}' is not available.")
   
   def return_movie(self, movie):
      if movie in self.borrowed_movies:
         self.borrowed_movies.remove(movie)
         MovieLibrary.available_movies.append(movie)
         print(f"{self.name} returned '{movie}'")
      else:
         print(f"{self.name} hasn't borrowed '{movie}'")

   def view_borrowed_movies(self):
      if self.borrowed_movies:
         print(f"{self.name} has borrowed: {', '.join(self.borrowed_movies)}")
      else:
         print(f"{self.name} has not borrowed any movies.")

member1 = MovieLibrary("Dhoni")
member1.borrow_movie("3 Idiots")
member1.view_borrowed_movies()
member1.return_movie("3 Idiots")
member1.view_borrowed_movies()      