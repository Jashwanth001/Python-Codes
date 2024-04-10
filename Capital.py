
#print("The Mountain".istitle()) == True
#print("The dog".istitle()) == False
#print("hello hi".istitle()) == False
"""
str1 = input("Enter a String:")
#print(len('str1'))
count = 0
for i in range(0,len(str1)):
    count+=1
print("The Lenght of the string is :",count)

#print('jashwanth'.count('a'))

#print('jashwanth'.capitalize())

str1 = input("Enter a String:")
if (str1.capitalize()):
    print("yes")
else:
    print("No")

str1 = int(input("Enter a String:"))
if ('str1'.isnumeric()==True):
    print("Yes")
else:
    print("No")

str1 =("Hello,i,am,jash")
print(str1.split('a'))


str1 = input("Enter a String:")
var = print(str1[0].islower()) == True
var = print(str1[0].isupper()) == False

#How to Add Two Numbers in Python – Easy Programs

num1 = int(input("Num1:"))
num2 = int(input("Num2:"))
num3 = num1 + num2
print('The sum is :',num3)


#Find Maximum of two numbers in Python

num1 = int(input("Num1:"))
num2 = int(input("Num2:"))

if num1>num2:
    print("Num1 is greater")
else:
    print("Num2 is greater")"""

#Python Program to Find the Factorial of a Number

def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 5
print("Factorial of", num, "is", factorial(num))








