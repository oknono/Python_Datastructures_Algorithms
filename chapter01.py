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

#R-1.4 - using resursion
def sum_of_squares(n):
	if n == 1:
		return 1
	else:
		return (n * n) + sum_of_squares(n-1)

#R-1.4 - using list comprehension
def sum_of_squares2(n):
	return sum(n * n for n in range(n + 1))