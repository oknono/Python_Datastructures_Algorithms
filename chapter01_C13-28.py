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
a
# print scale([1, 20, 300, 4000], 2)