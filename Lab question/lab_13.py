# 1. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist. 

def read_file(filename):
    try:
        with open(filename, 'r') as file: #file open in read mode
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


filename = "exception.txt"
read_file(filename)




# 2. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical


def check_number():
    try:
      num1=int(input("Enter First number: "))
      num2=int(input("Enter second number: "))
      print(f"Your First Number is {num1} and Second Number is {num2}")
    except ValueError as e:
      print("Entered input is not number :",e)


check_number()
