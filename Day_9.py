#Exercises: Level 1

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    wait = 18 - age
    print("Please you need to wait for " + str(wait) + " more year(s) to drive .")


#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 30
your_age = int(input("Enter your age: "))

if your_age == my_age:
    print("We are of the same age.")
elif your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print("You are " + str(difference) + " years older than me.")
else:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print("I am " + str(difference) + " years older than you.")

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")


#Exercises: Level 2


#1. Write a code which gives grade to students according to theirs scores:
	80-100, A
	70-89, B
	60-69, C
	50-59, D
	0-49, F

def assign_grade(score):
    if score >= 80 and score <= 100:
        return "A"
    elif score >= 70 and score <= 89:
        return "B"
    elif score >= 60 and score <= 69:
        return "C"
    elif score >= 50 and score <= 59:
        return "D"
    elif score >= 0 and score <= 49:
        return "F"
    else:
        return "Invalid score"

# Example usage
print(assign_grade(85)) # Output: A
print(assign_grade(75)) # Output: B
print(assign_grade(65)) # Output: C
print(assign_grade(55)) # Output: D
print(assign_grade(45)) # Output: F


#6.Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
def check_season(month):
    if month in ['September', 'October', 'November']:
        return "Autumn"
    elif month in ['December', 'January', 'February']:
        return "Winter"
    elif month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    else:
        return "Invalid month"

# Example usage
print(check_season("September")) # Output: Autumn
print(check_season("December")) # Output: Winter
print(check_season("April")) # Output: Spring
print(check_season("July")) # Output: Summer
print(check_season("XYZ")) # Output: Invalid month

#7. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = 'jacks fruits'
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else: 
    print('The fruit already exists in the list')


# Exercises: Level 3

#8. Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


if 'skills' in person:
    print(person['skills'][int(len(person['skills'])/2)])
    
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 


if 'skills' in person:
	    if 'Node' and 'MongoDB' in person['skills']:
	        if 'React' in person['skills']:
	            print('He is a fullstack developer')
	        elif 'Python' in person['skills']:
	            print('He is a backend developer')
	    elif 'JavaScript' and 'React' in person['skills']:
	        print('He is a frondend developer')
	    else: 
	        print('Unknown title')
	             

if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
first_name = person['first_name']
	last_name = person['last_name']
	country = person['country']
	

	if person['is_married']==True and person['country']=='Finland':
	    print(f'{first_name} {last_name} lives in {country}. He is married.')


