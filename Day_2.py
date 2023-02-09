 #2. Write a python comment saying 'Day 2: 30 Days of python programming' 
 comment = '30 days of python programming'

 #3.	Declare a first name variable and assign a value to it
first_name = 'Faisal Muhammad'

 #4.Declare a last name variable and assign a value to it
last_name = 'Adam'

 #5. 	Declare a full name variable and assign a value to it
full_name = 'Faisal Muhammad Adam'

# 6.	Declare a country variable and assign a value to it
country = 'Nigeria'

# 7.	Declare a city variable and assign a value to it
city = 'Kano'

# 8.	Declare an age variable and assign a value to it
age = 37

# 9.	Declare a year variable and assign a value to it
year = 1986

# 10.	Declare a variable is_married and assign a value to it
is_married = True

# 11.	Declare a variable is_true and assign a value to it
is_true = 'T'

# 12.	Declare a variable is_light_on and assign a value to it
is_light_on = 'Red'

# 13.	Declare multiple variable on one line
riga,kai,kafa = 'Wando','Hula','Takalmi'


		# level 2 exercise 
# 1. Using the len() built-in function, find the length of your first name
print(len(first_name))

# 2.	Compare the length of your first name and your last name
first_name = "Khadija"
last_name = "Faisal"

if len(first_name) > len(last_name):
    print("First name is longer than last name")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name")
else:
    print("First name and last name have the same length")

print(len(last_name) < len(first_name))

# 3.	Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#	Add num_one and num_two and assign the value to a variable total

num_one = 5
num_two = 4
total = num_one + num_two
print(total)

# Subtract num_two from num_one and assign the value to a variable diff 
num_one = 5
num_two = 4
diff = num_one - num_two


# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder

num_one = 5
num_two = 4
remainder = num_two % num_one

#Find floor division of num_one by num_two and assign the value to a variable floor_division
num_one = 5
num_two = 4
floor_division = num_one // num_two

# the radius of a circle is 30 meters.
i.	Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = 3.14 * (radius ** 2)

# ii.	Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
 radius = 30
circum_of_circle = 2 * 3.14 * radius

# iii.	Take radius as user input and calculate the area.
radius = int(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * (radius ** 2)

# 6.	Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print(f"Hello {first_name} {last_name} from {country}, your age is {age}")

#7.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

# some of the reserve keywords are 
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
