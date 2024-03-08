import re
def atoi(s):
	s = s.strip()
	if not s:
		return 0
	sign = -1 if s[0] == '-' else 1
	if s[0] in ['-','+']:
		s = s[1:]
	num = 0
	for char in s:
		if not char.isdigit():
			break
		num = num * 10 + int(char)
	return max(-2**31, min(sign * num, 2**31 - 1))

num = atoi("Bikram")
print(num)
