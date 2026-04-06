#1 print message 
a="hello world!"
print(a)

#2 Add two numbers
num1=5
num2=15
sum_result=num1+num2
print("the sum is:", sum_result)

#3 even or odd
num = int(input("Enter a number:"))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#4 cheak leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year") 

#5 print PI value
import math
print("The value of PI is:", math.pi)

#6 store and print constant value
MAX_LIMIT = 100
MIN_LIMIT = 1

print("Maximum Limit:", MAX_LIMIT)
print("Minimum Limit:", MIN_LIMIT)

#7 Square of a number
num = int(input("Enter a number: "))

square = num * num
print("Square of the number is:", square)

#8 Area of circle
PI = 3.14159

radius = float(input("Enter the radius of the circle: "))
area = PI * radius ** 2

print("Area of the circle is:", area)

#9 check data type
a = 10
b = 3.5
c = "Hello"
d = True

print(type(a))  
print(type(b))  
print(type(c))  
print(type(d))  

#10 use math function
num = float(input("Enter a number: "))
sqrt_value = math.sqrt(num)

print("Square root of the number is:", sqrt_value)

#11 find power
import math
num = float(input("Enter a number: "))
sqrt_value = math.sqrt(num)

print("Square root of the number is:", sqrt_value)

#12 check positive or negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")


