# 1.Write a decorator that counts the number of times a function has been called.

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


# 2.Write a decorator that repeats the execution of a function a specified number of times.

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
               result=func(*args, **kwargs)
            return result
        return wrapper
    return decorator
    
@repeat(5)
def my_data():
    print("Calling the function ")
    
my_data()