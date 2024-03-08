def length_of_longest_substring(s):
	max_length = 0
	char_map = {}
	start = 0
	for end, char in enumerate(s):
		if char in char_map and start <= char_map[char]:
			start = char_map[char] + 1
		else:
			max_length = max(max_length, end - start + 1)
		char_map[char] = end
	return max_length

st = length_of_longest_substring("ram narayan")
print(st)
