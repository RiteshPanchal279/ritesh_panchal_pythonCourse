# question 1
# Write a python program to reverse a number using a while loop.

def reverse(num):
    ans=0
    while num>0:
        last=num%10
        ans=ans*10+last
        num//=10
    return ans
num = int(input("Enter the number to reverse :"))
rev_ans=reverse(num)
print("reverse of ",num," is",rev_ans)

# question 2
# Write a python program to check whether a number is palindrome or not?

def isPalindrome(num):
    revNum = reverse(num)
    if(num==revNum):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

number=int(input("Enter the number for palindrome: "))
isPalindrome(number)