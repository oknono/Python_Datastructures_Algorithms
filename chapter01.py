#R-1.1
def is_multiple(n, m):
	return n % m == 0

#R-1.2 - Don't use modulo, division or multiplication. Assuming non-negative integer input
def is_even(k):
	if k == 1:
		return False
	elif k == 0:
		return True
	else:
	    return is_even(k-2)

# extra function for 1.6

def is_odd(k):
	return not is_even(k)

#R-1.3 - assumes input is a list of integers
def minmax(data):
	min = data[0]
	max = data[0]
	for item in data:
		if item < min:
			min = item
		if item > max:
			max = item
	return min, max

#R-1.4 - using resursion - n has to be larger than 1
# Fix this so it work for value 1
def sum_of_squares(n):
    return 0 if n == 1 else ((n - 1) * (n - 1)) + sum_of_squares(n-1)

#R-1.4
def sum_of_squares2(n):
	sum = 0
	for n in range(n):
		sum += n * n
	return sum


#R-1.4 - using list comprehension
#R-1.5
def sum_of_squares3(n):
	return sum(n * n for n in range(n))

#R-1.6
def sum_of_squares4(n):
		return sum(n * n for n in range(n) if is_odd(n) == True)