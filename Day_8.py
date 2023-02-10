#Exercises: Day 8

#1.Create an empty dictionary called dog
dog ={}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Duna Baleru'
dog['color'] = 'Black'
dog['breed'] = 'Shiba Inu'
dog['legs'] = 4
dog['age'] = 10

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'Abdurrahman'
student['last_name'] = 'Faisal'
student['gender'] = 'Male'
student['age'] = 3
student['marital_status'] = 'Single'
student['skills'] = ['Arithmetics', 'Alphabets', 'Drawing']
student['country'] = 'Kingdom of Saudi Arabia'
student['city'] = 'Jeddah'
student['address'] = 'No45 Al Faisaliyya District Main St'

#4. Get the length of the student dictionary
number_of_items = len(student)
print("Number of items in the dictionary:", number_of_items)

#5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
print("Value of skills:", skills)
print("Data type of skills:", type(skills))

#6. Modify the skills values by adding one or two skills
skills = student['skills']
print("Value of skills:", skills)
print("Data type of skills:", type(skills))
student['skills'] = student['skills'] + ['Verbal Reasoning', 'Quantitative Reasoning']
print("Updated skills:", student['skills'])

#7. Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary keys as a list:", keys)

#8. Get the dictionary values as a list

values = list(student.values())
print("Dictionary values as a list:", values)

#9. Change the dictionary to a list of tuples using items() method
student_list = list(student.items())
print("Dictionary as a list of tuples:", student_list)


#10. Delete one of the items in the dictionary
del student['city']
print("Dictionary after deletion:", student)

#11. Delete one of the dictionaries
Del student

