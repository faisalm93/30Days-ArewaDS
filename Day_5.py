#1. Declare an empty list
emptylist = []

#2. Declare a list with more than 5 items
emptylist= ["Kano", "Kaduna", "Borno", "Yobe", "Abuja"]

#3. Find the length of your list
print (len (emptylist))

#4. Get the first item, the middle item and the last item of the list
States = ["Kano", "Kaduna", "Borno", "Yobe", "Abuja"]
first_fruit = States[0] 
middle_fruit = States[2]
last_fruit = States[4]
print(first_fruit)      
print (middle_fruit)
print (last_fruit)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ( "Faisal", "35years", "1.75", "Married", "No1 Naibawa Quartesr")

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ("Google", "Microsoft", "Apple", "IBM", "Oracle", "AMazon")


#7. Print the list using print() 
print (it_companies)

#8. Print the number of companies in the list
print (len (it_companies))

#9. Print the first, middle and last company
first_it_company = it_companies[0] 
middle_it_company = it_companies[2]
last_it_company = it_companies[4]
print(first_it_company)      
print (middle_it_company)
print (last_it_company)

# 10.	Print the list after modifying one of the companies
it_companies = ("Arewa DataSCience", "Microsoft", "Apple", "IBM" "Oracle", "AMazon")
print (len (it_companies))
first_it_company = it_companies[0] 
middle_it_company = it_companies[2]
last_it_company = it_companies[4]
print(first_it_company)      
print (middle_it_company)
print (last_it_company)

# 11.	Add an IT company to it_companies

it_companies = ("Arewa DataSCience", "Microsoft", "Apple", "IBM" "Oracle", "AMazon", "Hausa NLP")
print (len (it_companies))
first_it_company = it_companies[0] 
middle_it_company = it_companies[2]
last_it_company = it_companies[5]
print(first_it_company)      
print (middle_it_company)
print (last_it_company)

# 12.	Insert an IT company in the middle of the companies list
it_companies = ("Arewa DataSCience", "Microsoft", "Traxon Technoloies","Apple", "IBM" "Oracle", "AMazon", "Hausa NLP")
print (len (it_companies))
first_it_company = it_companies[0] 
middle_it_company = it_companies[2]
last_it_company = it_companies[6]
print(first_it_company)      
print (middle_it_company)
print (last_it_company)

# 13.	Change one of the it_companies names to uppercase (IBM excluded!)

it_companies = ("Arewa DataSCience", "Microsoft", "Traxon Technoloies","Apple", "IBM" "Oracle", "AMazon", "Hausa NLP")
print (len (it_companies))
first_it_company = it_companies[0] 
middle_it_company = it_companies[2]
last_it_company = it_companies[6]
print(first_it_company)      
print (middle_it_company)
print (last_it_company)

# 13. Check if a certain company exists in the it_companies list.
'Facebook' in it_companies # False: Changed it, remember

# 14. Sort the list using sort() method
it_companies.sort() # method returns none
print(it_companies)

# 15. Reverse the list in descending order using reverse() method
it_companies.reverse() # also returns none
print(it_companies)

# 16. Slice out the first 3 companies from the list
it_companies[:3]

# 17. Slice out the last 3 companies from the list
it_companies[-3:]

# 17. Slice out the middle IT company or companies from the list
it_companies[len(it_companies)//2:len(it_companies)//2+1]

# 18. Remove the first IT company from the list
it_companies.pop(0)
it_companies

# 19.  Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies)/2))

# 20. Remove the last IT company from the list
it_companies.pop()

# 21. Remove all IT companies from the list
it_companies.clear()
it_companies

# 22. Destroy the IT companies list
del it_companies
it_companies

# 23. Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)
# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy() # front_end contains the two lists
# first find the index of redux
full_stack.index('Redux') # 4
full_stack.insert(5,'Python') # insertion is done before the index
full_stack.insert(full_stack.index('Python')+1,'SQL')
full_stack # worked!!! I'll get better with practise

#Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)  # worked
min_age = min(ages)  # 19
max_age = max(ages)  # 26
print(f'The minimum age is {min_age} and the maximum age is {max_age} ')
# Add the min age and the max age again to the list
ages.extend([19,26])
ages

# 2. Find the median age (one middle item or two middle items divided by two)
ages.sort()
ages_length = len(ages)
len(ages)
print(ages[int(len(ages)/2-1)],ages[int(len(ages)/2)]) # 24,24

if ages_length % 2 == 0:
  cond1 = ages[ages_length//2]
  cond2 = ages[ages_length//2-1]
  median_age = (cond1 + cond2)/2

else: 
  median_age = ages[ages_length//2]
print(f'The median age of the ages is {median_age}')

# 3. Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages) # 22.75
print(f'The average age is {average}')

# 4. Find the range of the ages (max minus min)
rng = max(ages) - min(ages) # 7
print(f'The range of the ages is {rng}')

# 5.  Compare the value of (min - average) and (max - average), use abs() method 
abs(min(ages) - average) == abs(max(ages)- average) # not equal

# 6. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
countries.sort()
countries_length = len(countries)

if countries_length % 2 == 0:
  cond1 = countries[countries_length//2]
  cond2 = countries[countries_length//2-1]
  middle_country = (cond1 , cond2)

else: 
  middle_country = countries[countries_length//2]
print(f'The mid country in the countries list is {middle_country}')

mid_country = countries[len(countries)//2]
print(f'The middle country in the list is {mid_country} ') # Lesotho
# confirming with index
countries.index('Lesotho') # index is 96 : correct. Lesotho is the 97th out of the 193 countries.

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_length = len(countries) # 193 = odd
first_half = countries[:countries_length//2]
second_half = countries[countries_length//2:]
first_half_length = len(first_half)
second_half_length = len(second_half)

print(f'The length of the two halves are {first_half_length} and {second_half_length} ')



# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.
CH,RU,US,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic
print(f'The scandic countries in the last list given are {scandic}')