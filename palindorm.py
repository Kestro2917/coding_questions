def is_palindrom(x):
	if x < 0:
		return False
	reversed_x = int(str(x)[::-1])
	return x == reversed_x

ch = is_palindrom(101)
print(ch)
