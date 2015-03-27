# C-1.13 - Write a pseudo-code description of
# a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order
# than they were before, and compare this method to an equivalent Python
# function for doing the same thing.

# python build-in : print name_list.reverse()


def reverse_list(data):
	new_list = []
    for index in range(1, len(data) + 1):
        new_list.append(data[-index])
    return new_list


# C-1.14 Write a short Python function that takes a sequence of integer
# values and determines if there is a distinct pair of numbers in the
# sequence whose product is odd.


def odd_sequence(data):
    for index in range(len(data)):
        if is_odd(data[index] * data[index + 1]):
            return index, index + 1


def is_odd(k):
    return k % 2 != 0


# C-1.15 Write a Python function that takes a sequence of numbers
# and determines if all the numbers are different from each other
# (that is, they are distinct)


def unique(data):
    new_list = []
    for index in range(len(data)):
        if data[index] in new_list:
            return False
        else:
            new_list.append(data[index])
    return True


# C-1.16 
# def scale(data, factor):
#     for j in range(len(data)):
#          data[j] ￼ = factor
# In this function we manipulate a list element - chaging the list
# list and scale(list,factor) have smae ID
# With function with exercise, a None is returned

# C-1.18
# List comprehension, start with 0 end with 90, + 2, +4, +6, +8 etc.
# Basically list is product of list1 = range(10)[0 ..9] 
# and list2 = range(1,11) [1..10]

# print [ n * (n - 1) for n in range(1, 11)]

# C-1.19
# Ascii for 'a' to 'z' is 97 - 122. Char(97) gives 'a'
# ord('a') gives 97

# print [chr(n) for n in range(97, 123)]

if __name__ == "__main__":
    print reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    print odd_sequence([1, 2, 3, 7]) == (2, 3)
    print unique([1, 2, 3, 4]) == True
    print unique([1, 2, 3, 4, 2, 0]) == False
