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
