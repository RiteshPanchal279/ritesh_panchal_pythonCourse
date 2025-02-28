def get_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Error : invalid input")

num1 = get_input("Enter first inetger: ")
num2 = get_input("Enter second integer: ")
mul = num1*num2
print("Product of two numbers:", mul)

add = num1+num2
print("Sum of two numbers:", add)

sub = num1-num2
print("Subtraction of two numbers:", sub)

div = num1/num2
print("Division of two numbers:", div)

mod = num1%num2
print("Modulo of two numbers:", mod)