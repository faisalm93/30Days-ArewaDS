#Exercises: Level 1

#1. Iterate 0 to 10 using for loop, do the same using while loop.
for Z in range(11):
    print(Z)
p = 0
while p <= 10:
    print(p)
    p = p + 1

# 2.	Iterate 10 to 0 using for loop, do the same using while loop.
for u in reversed(range(11)):
    print(u)
y = 10
while y >= 0:
    print(y)
    y = y - 1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
y = 10
while y >= 0:
    print(y)
    y = y - 1
for i in range(1, 8):
    print("#" * i)

#4. Use nested loops to create the following:
y = 10
while y >= 0:
    print(y)
    y = y - 1
for i in range(1, 8):
    print("#" * i)
for i in range(7):
    for j in range(8):
        print("#", end=" ")
    print()

#5. Print the following pattern:
	0 x 0 = 0
	1 x 1 = 1
	2 x 2 = 4

for i in range(3):
    print(f"{i} x {i} = {i*i}")


#6. 29.	Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for X in range(101):# i use 101 becouse the count will start from index 0
    if X % 2 == 0:
        print(X)

#8.Use for loop to iterate from 0 to 100 and print only odd numbers

for i in range(101):
    if i % 2 != 0: # 
        print(i)

#Exercises: Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
The sum of all numbers is 5050.
total = 0
for Z in range(101):
    total += Z
print("The sum of all numbers from 0 to 100 is", total)


#2.  Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
The sum of all evens is 2550. And the sum of all odds is 2500.
total_even = 0
total_odd = 0
for y in range(101):
    if y % 2 == 0:
        total_even += y
    else:
        total_odd += y
print("The sum of all even numbers from 0 to 100 is", total_even)
print("The sum of all odd numbers from 0 to 100 is", total_odd)



#Exercises: Level 3

#1.Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.


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

];
land_countries = []
for country in countries:
    if 'land' in country:
        land_countries.append(country)
print("Countries containing the word 'land':", land_countries)


#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in reversed(fruits):
    reversed_fruits.append(fruit)
print("Reversed order of fruits:", reversed_fruits)

