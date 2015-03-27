# C-1.13 - Write a pseudo-code description of 
# a function that reverses a list of n integers, 
# so that the numbers are listed in the opposite order 
# than they were before, and compare this method to an equivalent Python 
# function for doing the same thing.

# python build-in : print name_list.reverse()

def reverse_list(data):
	new_list = []
	for index in range(1, len(data)+ 1):
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


if __name__ == "__main__":
	print reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
	print odd_sequence([1, 2, 3, 7]) == (2, 3)
