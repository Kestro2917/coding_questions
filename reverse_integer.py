def reverse_integer(x):
	if x < 0:
		return -reverse_integer(-x)
	rev = 0
	while x != 0:
		rev = rev * 10 + x % 10
		x //= 10
	return rev if rev <= 2**31-1 else 0

x = reverse_integer(10)
print(x)
