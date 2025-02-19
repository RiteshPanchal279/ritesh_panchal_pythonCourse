# finding the grater form Four without using logical operator 
num1=223
num2=344
num3=102
num4=530

if(num1>num2):
   if(num1>num3):
      if(num1>num4):
         print("Greatest no: ", num1)
      else:
         print("Greatest no: ", num4)
   else:
      print("Greatest no: ", num3)
else:
   if(num2>num3):
      if(num2>num4):
         print("Greatest no: ", num2)
      else:
         print("Greatest no: ", num4)
   else:
      print("Greatest no: ", num3)

   