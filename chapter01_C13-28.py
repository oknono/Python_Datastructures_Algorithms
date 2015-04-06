import random 

# C-1.13 

def reverse_list(data):
    new_list = []
    for index in range(len(data)): # 0, 1, 2, 3 -> -1, -2, -3, -4
        new_list.append(data[(index * -1) - 1])
    return new_list

# print reverse_list([1, 20, 300, 4000])

# C-1.14 Write a short Python function that takes a sequence of integer
# values and determines if there is a distinct pair of numbers in the
# sequence whose product is odd. - Stops after first pair.

def odd_sequence(data):
    for index in range(len(data)):
        if is_odd(data[index] * data[index + 1]):
            return index, index + 1

def is_odd(k):
    return k % 2 != 0

# print odd_sequence([1,2,3,4,5,8,9,11,14,15,19])


# C-1.15 Write a Python function that takes a sequence of numbers
# and determines if all the numbers are different from each other
# (that is, they are distinct)

def no_duplicates(data):
    new_list = []
    for index in range(len(data)):
        if data[index] in new_list:
            return False
        else:
            new_list.append(data[index])
    return True

# print no_duplicates([])
# print no_duplicates([1, 2, 3, 4, 5, 6])
# print no_duplicates([1, 2, 3, 4, 5, 6, 4])

# C-1.16 and  # C-1.17
# NO - directly manipulating object

# C-1.18
# List comprehension, start with 0 end with 90, + 2, +4, +6, +8 etc.
# Basically list is product of list1 = range(10) -> [0 ..9] 
# and list2 = range(1,11) -> [1..10]

# print [ n * (n - 1) for n in range(1, 11)]

# C-1.19
# Ascii for 'a' to 'z' is 97 - 122. Char(97) gives 'a'
# ord('a') gives 97

# print [chr(n) for n in range(97, 123)]

# C-1.20 Shuffle a list using only randint(begin, end)
# start with a list - reassign each item to a new index.
# We swap first element with random element, second with
# random element etc.

def new_shuffle(data):
    for index in range(len(data)):
        new_index = random.randint(0, len(data) - 1)
        data[index], data[new_index] = data[new_index], data[index]
    return data

print new_shuffle([1, 2, 3, 4])
# C-1.21 TO DO


# C-1.22 Write a short Python program that takes two arrays a and b of length n storing
# int values, and returns the dot product of a and b
def multiply_list(data1, data2):
    data3 = []
    for index in range(len(data1)):
        data3.append(data1[index]*data2[index])
    return data3

# print multiply_list([1,2,3,4,5,6],[2,3,4,5,6,7])

# C-1.23 TO DO

# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.

def count_vowel(word):  
    return sum(1 for letter in word if letter in 'aeoui')

# print count_vowel('apple tree ') 

# C-1.25 WriteashortPythonfunctionthattakesastrings,representingasentence,
# and returns a copy of the string with all punctuation removed.
def remove_punctuation(word):
    return ''.join(letter for letter in word if letter not in "\"\'\,\.\:\;\?\!")

# print remove_punctuation("Let's try, Mike.")

# C-1.26 Write a short program that takes as input three integers, a, b, and c,
# from the console and determines if they can be used in a correct arithmetic formula
def correct(a, b, c):
    return (a + b == c) or (b + c == a) or (a + c == b) or (a * b == c) or \
           (a * c == b) or (b * c == a)

# print correct(3,2,1)
# print correct(1,4,2)

# C-1.27 TO DO
# C-1.28 TO DO

