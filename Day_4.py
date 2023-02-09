# 1.	Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

text = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
# you can print print(text) to see the outcome

#2.	Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
text = ' '.join(['Coding', 'For', 'All, '])

#3.	Declare a variable named company and assign it to an initial value "Coding For All".
Company = ”Coding For All”

#4.	Print the variable company using print().
Print (Company)

#5.	Print the length of the company string using len() method and print().
Print( len (Company))

#6.	Change all the characters to uppercase letters using upper() method.
company = "coding for all"
uppercase_company = company.upper()
# you can print (uppercase_company) to see changes.

#7.	Change all the characters to lowercase letters using lower() method.

company = "CODING FOR ALL"
lowercase_company = company.lower()

# you can print (lowercase_company) to see changes.

# 8.	Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
string = "Coding For All"

string = "Coding For All"

# capitalize() method
capitalized_string = string.capitalize()
print(capitalized_string)

# title() method
title_string = string.title()
print(title_string)

# 9.Cut(slice) out the first word of Coding For All string.
show = "Coding For All"
first_word = show[:6]

# You can print(first_word) to see changes.


10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
b = "Coding For All"
check = "Coding" in b
print(check)

check = a.find("Coding")
# print(check)to see changes

#11. Replace the word coding in the string 'Coding For All' to Python.
a = "'Coding For All"
new_a = a.replace("Coding", "Python")
print(new_a)

#12.	Change Python for Everyone to Python for All using the replace method or other methods.
z = "Python for Everyone"
new_z = z.replace("Python for Everyone", "Python for All")
print(new_z)

#13. Split the string 'Coding For All' using space as the separator (split()) .
string = "Coding For All"
splitted_string = string.split()
print(splitted_string)

# 14.	"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "FAcebook Google Microsoft APPle IBM Oracle Amazon"
splitted_string = string.split()
print(splitted_string)


# 15.What is the character at index 0 in the string Coding For All.
print('Coding For All'[0])   # assigning will waste typing time if string will be used only once
print(company[0]) # letter C

#16.What is the last index of the string Coding For All.

#The character at index 13 in the str 'Coding For All' is: l
str = "Coding For All"
index = 13
print("The character at index", index, "in the str '" + str + "' is:", str[index])


#17.	What character is at index 10 in "Coding For All" string.
#The character at index 10 in the str 'Coding For All' is:  white space

# 19.	Create an acronym or an abbreviation for the name 'Coding For All'.
def abbreviate(text):
    words = text.split()
    abbreviation = ""
    for word in words:
        abbreviation += word[0].upper()
    return abbreviation

text = "Coding for All"
abbreviation = abbreviate(text)
print(abbreviation)

# 20.	Use index to determine the position of the first occurrence of C in Coding For All.
C_position = "Coding For All"
first_occurrence = C_position.index("C")
print(first_occurrence)

# 21.	Use index to determine the position of the first occurrence of F in Coding For All.
F_position = "Coding For All"
first_occurrence = F_position.index("F")
print(first_occurrence)

# 22.	Use rfind to determine the position of the last occurrence of l in Coding For All People.
rfind = "Coding For All"
last_occurrence = rfind.rfind("l")
print(last_occurrence)

# 23.	Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find = 'You cannot end a sentence with because because because is a conjunction'
First_occurance = Find.rfind('because')
print (First_occurance)


# 24.	Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
last_occurrence = sentence.rindex("because")
print(last_occurrence)

# 25.	Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
start_index = sentence.index("because")
end_index = start_index + len("because because because")
phrase = sentence[start_index:end_index]
print(phrase)

# 26.	Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Position = 'You cannot end a sentence with because because because is a conjunction'
First_occurance = Position.rfind('because')
print (First_occurance)

# 28.	Does ''Coding For All' start with a substring Coding?
A = "Coding For All"
check = A.startswith("Coding")
print(check)

# 29.	Does 'Coding For All' end with a substring coding?
b = "Coding For All"
check = b.endswith("Coding")
print(check)
# 30.	'   Coding For All      '  , remove the left and right trailing spaces in the given string.
Y = "   Coding For All   "
Y2 = Y.strip()
print(Y2)


#31.	Which one of the following variables return True when we use the method isidentifier():
o	30DaysOfPython
o	thirty_days_of_python
#the first will return True while the second will return false
identifier_1 = "thirty_days_of_python"
identifier_2 = "30DaysOfPython"
print(identifier_1.isidentifier()) 
print(identifier_2.isidentifier()) 


#32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
Pythonlibrary = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = "# ".join(Pythonlibrary)
print(joined_string)

# 33.	Use the new line escape sequence to separate the following sentences.
I am enjoying this challengeI just wonder what is next.

sentence_1 = "I am enjoying this challenge."
sentence_2 = "I just wonder what is next."

print(sentence_1 + "\n" + sentence_2)

# 34.	Use a tab escape sequence to write the following lines.
lines = "Name\tAge\tCountry\tCity"
print(lines)


# 35.	Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2

result = "The area of a circle with radius {} is {:.0f} meters square.".format(radius, area)
print(result)


#36.	Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
result_1 = "8 + 6 = {}".format(8 + 6)
result_2 = "8 - 6 = {}".format(8 - 6)
result_3 = "8 * 6 = {}".format(8 * 6)
result_4 = "8 / 6 = {:.2f}".format(8 / 6)
result_5 = "8 % 6 = {}".format(8 % 6)
result_6 = "8 // 6 = {}".format(8 // 6)
result_7 = "8 ** 6 = {}".format(8 ** 6)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)
print(result_7)



