 # 1. Check the python version you are using
python -V

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.

print(3+4) # addition
print(3-4) # subtraction
print(3*4) # multiplication
print(3 % 4) # modulos
print(3/4) # division
print(3**4) # exponentiation
print(3//4) # floor division

# 3. Write strings on the python interactive shell. The strings are the following:
first_name = "Faisal"
print(first_name)

family_name = "Adam"
print(family_name)

country = "Nigeria"
print(country)
print('I am enjoying 30 days of python')

# 4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))

# Level 3 exercise
# Integer
age = 25
print(age)

# Float
weight = 78.5
print(weight)

# Complex
x = 3+5j
print(x)

#Strings Data types
name = "Abdurrahman Faisal"
print(name)

#Boolean Data type
is_student = True
print(is_student)

#List data type
fruits = ["apple", "banana", "orange"]
print(fruits)

#Tupples
coordinates = (2, 3)
print(coordinates)

#Set
numbers = {1, 2, 3, 4}
print(numbers)

#Dictionary
person = {"name": "Lado", "age": 30, "city": "Kano"}
print(person)


#euclidian distance

import math

point1 = (2, 3)
point2 = (10, 8)

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

print(distance)
