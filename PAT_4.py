'''Q7
import math
num = int(input("Enter a Number:"))
sqr = math.sqrt(num)
print("The Square is:",round(sqr))


#Q8
num1 = int(input("Num1:")) #5
num2 = int(input("Num2:")) #10

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Num1:",num1)
print("Num2:",num2)



#Q9
num = int(input("Num:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")


#Q10
num = int(input("Enter a Number:"))
if num%400==0:
    print(num," is a Leap Year")
elif num%100!=0 and num%4==0:
    print(num,"is a Leap Year")
else:
    print(num,"is Not a Leap Year")


#Q11
name = input("Name of the Student:")
sum=0
for i in range(0,3):
    mark = int(input("Marks of Student:"))
    sum+=mark
    avg = sum/3
print(avg,"average marks in 3 subjects")


#Q12
name = input("Name of the Student:")
size = int(input("How many marks to enter"))
sum=0
for i in range(0,size):
    mark = int(input("Marks of Student:"))
    sum+=mark
    avg = sum/3
if avg>65:
    print("Pass")
else:
    print("Fail")


#Q13
celsius = int(input("Celsius:"))
# (°C x 1.8) + 32
F = (celsius * 1.8) + 32
print(F,"is the Fahrenheit")


#Q14
# km = (n × 0.62137119)
n = int(input("Kilometers:"))
km = (n * 0.62137119)
print(km,"is the miles")
'''

#Q15


