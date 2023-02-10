# Exercises: Level 1

#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(y, z):
    return y + z
result = add_two_numbers(6, 4)
print(result)

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
import math # math module was imported so as to provides access to the constant pi. 

def area_of_circle(radius):
    return math.pi * radius * radius
area = area_of_circle(2)
print(area) # this will calculate and print circle within a radius of 2


#3.  Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args): # this syntax enable us to pass a variable number of arguments to a function.
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Error: All arguments must be numbers."
    return sum(args)
result = add_all_nums(1, 2, 3, 4, 5)
print(result) # Output: 15

result = add_all_nums(1, 2, 3, 4, 5, "six")
print(result) # Output: "Error: All arguments must be numbers."


#.4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
fahrenheit = convert_celsius_to_fahrenheit(25)
print(fahrenheit) # Output will be: 77.0


#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid Month"

month = int(input("Enter a month (as a number): "))
season = check_season(month)
print("The season is:", season)


#6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope = calculate_slope(x1, y1, x2, y2)

print("The slope of the line passing through the points ({}, {}) and ({}, {}) is: {}".format(x1, y1, x2, y2, slope))

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solution"
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]

#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
my_list = [10, 11, 13, 14, 15]
print_list(my_list)

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reversed_list)

#10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_list = []
    for item in lst:
        capitalized_list.append(item.capitalize())
    return capitalized_list

my_list = ["apple", "banana", "cherry"]
capitalized_list = capitalize_list_items(my_list)
print(capitalized_list)

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(lst, item):
    lst.append(item)
    return lst
my_list = [1, 2, 3, 4, 5]
new_list = add_item(my_list, 6)
print(new_list)


#12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lst, item):
    lst.remove(item)
    return lst
my_list = [1, 2, 3, 4, 5]
new_list = remove_item(my_list, 3)# 3 will be remove
print(new_list)

#13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def remove_item(lst, item):
    lst.remove(item)
    return lst
my_list = [1, 2, 3, 4, 5]
new_list = remove_item(my_list, 3)# 3 will be remove
print(new_list)

def sum_of_numbers(n):
    return sum(range(1, n + 1))
result = sum_of_numbers(5)
print(result)

#14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
result = sum_of_odds(5)
print(result)


#15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    sum = 0
    for i in range(2, number+1, 2):
        sum += i
    return sum
print(sum_of_even(10))



	#Exercises: Level 2
#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    even_count = 0
    odd_count = 0
    for i in range(1, number+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(parameter):
    return not bool(parameter)
parameter = input("Enter a parameter: ")
result = is_empty(parameter)
if result:
    print("The parameter is empty.")
else:
    print("The parameter is not empty.")

#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(list):
  sum = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  return mean
print(f'The mean of [1,2,3,4,5]: {calculate_mean([1,2,3,4,5])}')

def calculate_median(list):
  list_length = len(list)
  list.sort()
  if list_length % 2 == 0:
    median = (list[list_length//2] + list[list_length//2 - 1])/2
  else:
    median = list[list_length//2]
  return median

print(f'The median of [1,3,4,5,2]: {calculate_median([1,3,4,5,2])}')
print(f'The median of [1,4,3,2]: {calculate_median([1,4,3,2])}')

def calculate_mode(list):
  dic = {}
  for item in list:
      dic[item] = dic.get(item,0) + 1
  return [i for  i,j in dic.items() if j == max(dic.values()) ]
    
print(f'The mode of [1,1,1,3,4,5,6,6,6,8,8,1,1]: {calculate_mode([1,1,1,3,4,5,6,6,6,8,8,1,1])}')

def calculate_range(list):
  list.sort()
  range = list[len(list)-1] - list[0]
  return range
print(f'The range of [10,90,5,3,6,7]: {calculate_range([10,90,5,3,6,7])}')

def calculate_variance(list):
  sum = 0
  sum_of_diffs = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  for i in range(len(list)):
    sum_of_diffs +=  (list[i] - mean ) ** 2
  variance = sum_of_diffs/(len(list) - 1)
  return variance

print(f'The variance of [1,2,4,5,6,7,8]: {calculate_variance([1,2,4,5,6,7,8])}')

def calculate_std(list):
  sum = 0
  sum_of_diffs = 0
  for i in range(len(list)):
    sum += list[i]
  mean = sum / len(list)
  for i in range(len(list)):
    sum_of_diffs +=  ((list[i] - mean ) ** 2)
  sd = (sum_of_diffs/(len(list)-1)) ** (1/2)
  return sd

print(f'The sd of [1,2,4,5,6,7,8] : {calculate_std([1,2,4,5,6,7,8])}')


#Exercises: Level 3

#1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it's prime: ")) # the block is added just to make things work better
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


#2. Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    return len(lst) == len(set(lst))

my_list = [1, 2, 3, 4, 5]
if is_unique(my_list):
    print("All items in the list are unique")
else:
    print("Some items in the list are not unique")


#3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    if len(lst) == 0:
        return True
    first_item_type = type(lst[0])
    for item in lst:
        if type(item) != first_item_type:
            return False
    return True

#4. Write a function which check if provided variable is a valid python variable

def is_python_variable(name):
    if name[0] not in ['0','1','2','3','4','5','6','7','8','9'] and ' ' not in name:
       result = 'A valid variable name'
    else:
      result = 'Not a valid variable name'
    return result


#5. Go to the data folder and access the countries-data.py file.
	#Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
