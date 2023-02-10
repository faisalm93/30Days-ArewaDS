		#Exercises: Day 12

#Exercises: Level 1

#1. Write a function which generates a six digit/character random_user_id.
import random
import string
def random_user_id():
    return "".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6))

print(random_user_id())

#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.


# Testing this for my function
["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6)) for j in range(6)]



def random_user_id_gen_by_user():
    a = int(input("Enter the number of characters: "))
    b = int(input("Enter the number of IDs: "))
    return ["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(a)) for j in range(b)]

# unpack operator in print function    #learning bonus
s =["".join(str(random.choice(string.ascii_letters + string.digits)) for i in range(6)) for j in range(6)]
print(*s,sep='\n')
#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

	#Exercises: Level 2
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string

def list_of_hexa_colors(num_colors):
    hexa_chars = string.digits + 'abcdef'

    hexa_colors = []
    for _ in range(num_colors):
        color = '#'
        for _ in range(6):
            color += random.choice(hexa_chars)
        hexa_colors.append(color)

    return hexa_colors

#2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append((r, g, b))
    return colors

#3. Write a function generate_colors which can generate any number of hexa or rgb colors.

import random

def generate_colors(n, format='RGB'):
    colors = []
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if format == 'RGB':
            colors.append((r, g, b))
        elif format == 'HEX':
            hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            colors.append(hex_color)
    return colors


	#Exercises: Level 3
#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(input_list):
    random.shuffle(input_list)
    return input_list

# Call the function and store the result in a variable
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffled_list = shuffle_list(my_list)
print(shuffled_list)

# Call the function and use the result directly
print(shuffle_list([10, 20, 30, 40, 50, 60, 70]))

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def unique_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers
