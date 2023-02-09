#1. Declare your age as integer variable
Age = 37

#2. Declare your height as a float variable
Height = 12.5

#3. Declare a variable that store a complex number
Complex_number = 22- 459*4, 

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is:", perimeter)

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
def equation(x):
    return 2*x - 2

slope = 2
x_intercept = 0
y_intercept = -2
print("The slope of the equation is:", slope)
print("The x-intercept of the equation is:", (x_intercept, equation(x_intercept)))
print("The y-intercept of the equation is:", (-equation(0)/slope, 0))

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope
m = (y2 - y1) / (x2 - x1)
print(f"The slope of the line between points ({x1}, {y1}) and ({x2}, {y2}) is {m}")

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"The Euclidean distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}")

#10.Compare the slopes in tasks 8 and 9
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_equation = 2
slope_points = (y2 - y1) / (x2 - x1)

if slope_equation == slope_points:
    print("The slopes are the same.")
else:
    print("The slopes are different.")
# for the above comparison, the slopes are the same.



#11.	Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.


x = int(input("Value of x: "))
y = x ** 2 + 6 * x + 9
print("Value of y: ", y)
import math

a = 1
b = 6
c = 9

x = [0, 1, 2, 3, 4,5,6,7,-3]

for i in x:
    y = a * i**2 + b * i + c
    print("For x =", i, "y =", y)

d = b**2 - 4*a*c
x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print("x1 =", x1)
print("x2 =", x2)
# When x=-3, y will be 0

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement
python = 'python'
dragon = 'dragon'

length_python = len(python)
length_dragon = len(dragon)

if not length_python == length_dragon:
    print("The length of 'python' is not equal to the length of 'dragon'.")
else:
    print("The length of 'python' is equal to the length of 'dragon'.")

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
string1 = 'python'
string2 = 'dragon'

if 'on' in string1 and 'on' in string2:
    print("'on' is found in both strings.")
else:
    print("'on' is not found in both strings.")

# 14.I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."

if 'jargon' in sentence:
    print("'jargon' is in the sentence.")
else:
    print("'jargon' is not in the sentence.")

# 15 Find the length of the text python and convert the value to float and convert it to string

text = 'python'

length = len(text)
length_float = float(length)
length_str = str(length_float)

print("Length of text as int:", length)
print("Length of text as float:", length_float)
print("Length of text as string:", length_str)

#16. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 7

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# 17.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
result = 7 // 3
compare = int(2.7)

if result == compare:
    print("The floor division is equal to the int-converted value.")
else:
    print("The floor division is not equal to the int-converted value.")

#18.	Check if type of '10' is equal to type of 10

 a = '10'
b = 10

if type(a) == type(b):
    print("The types are equal.")
else:
    print("The types are not equal.")

#19.Check if int('9.8') is equal to 10
f = '9.8'
g = 10

if type(f) == type(g):
    print("The types are equal.")
else:
    print("The types are not equal.")

#20 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate

print("Pay:", pay)

# 21.Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years: "))
seconds = years * 365 * 24 * 60 * 60

print("Number of seconds a person can live:", seconds)


#22.	Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125


print("x y")
for i in range(1, 6):
    row = [str(i), str(i**1), str(i**2), str(i**3), str(i**4), str(i**5)]
    print(" ".join(row))


