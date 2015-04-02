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

# C-1.16  and C-1.17 _ TODO
# In this function we manipulate a list element - changing the list.
# List and scale(list,factor) have same ID
# With function with exercise, a None is returned

# def scale(data, factor):
#    for j in range(len(data)):
#        data[j] *= factor
#
# print scale([1, 20, 300, 4000], 2)

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
# We start with n possible indices, and these shrink
# The issue I have is that I can't say between 1 and 5, but not three
# If I need to reuse indices, best way to do so. Every element needs to be in new list
# TO DO

# C-1.21 TO DO


# C-1.22 Write a short Python program that takes two arrays a and b of length n storing
# int values, and returns the dot product of a and b
def multiply_list(data1, data2):
    data3 = []
    for index in range(len(data1)):
        data3.append(data1[index]*data2[index])
    return data3

# print multiply_list([1,2,3,4,5,6],[2,3,4,5,6,7])