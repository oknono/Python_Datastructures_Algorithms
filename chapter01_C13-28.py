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

if __name__ == "__main__":
	print reverse_list([1, 2, 3, 4])