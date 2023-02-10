# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

Exercises: Level 1
# 1. Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies) # the answer should be 7

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

#3. Insert multiple IT companies at once to the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
other_companies = {'Twitter', 'Alibaba', 'Netflix'}
it_companies.update(other_companies)

#4. Remove one of the companies from the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon'}
it_companies.discard('Apple')

#5. What is the difference between remove and discard
The difference is that ## If Apple is not found remove() method will raise errors, while if discard method is use, there will be no error even Apple was not found.


#Exercises: Level 2
#1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B) ## the result should be {19, 20, 22, 24, 25, 26, 27, 28}

#2. Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.intersection(B) ## the result should be {19, 20, 22, 24, 25, 26}


#3. Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.issubset(B) ## A is a subset of B and the answer is True

#4. Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.isdisjoint(B) ## both A and B has common numbers. Therefore, the outcome should be False

#5. Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = B.union(A)

#6. What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.symmetric_difference(B)
# The symmetric difference between A and B is {27, 28}

#7.Delete the sets completely
# We can use the del () function to delete the sets


#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
set = set(age)

if len(age) > len(set):
    print("The list is bigger than the set.")
else:
    print("The set is bigger than the list.")

#2. Explain the difference between the following data types: string, list, tuple and set
A string is any given data that’s is written text enclose in a single, double or triple quote. Once written, it can’t be changed. i.e. immutable
List is a collection which is ordered and changeable(modifiable). Allows duplicate members. They Lists are mutable, which means that their contents can be changed after they are created.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members. They are often used to store collections of values that should not be modified, such as dates or other pieces of information.
Set is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed. They are mutable, which means that their contents can be changed after they are created.

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)
print("Number of unique words:", number_of_unique_words)

