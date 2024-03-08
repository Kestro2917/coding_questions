def roman_to_int(s):
	roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	num = 0
	prev_value = 0
	for char in s[::-1]:
		curr_value = roman_map[char]
		if curr_value >= prev_value:
			num += curr_value
		else:
			num -= curr_value
		prev_value = curr_value
	return num
num = roman_to_int("IX")
print(num)
