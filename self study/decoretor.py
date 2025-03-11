# Write a decorator that counts the number of times a function has been called.

def decorator(func):
   count=0
   def wrapper(*args,**kwargs):
      nonlocal count
      count+=1
      print("Functio call this time: ",count)
      return func(*args,**kwargs)
   return wrapper


@decorator
def check():
   print("The check function call")
   
check()
check()
check()
check()