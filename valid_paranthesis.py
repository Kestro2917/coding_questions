def is_valid(s):
	stack = []
	bracket_map = {')':'(','}':'{',']':'['}
	for char in s:
		if char in s:
			stack.append(char)
		elif char in bracket_map.keys():
			if not stack or bracket_map[char] != stack.pop():
				return False
		else:
			return False
	return not stack
is_valid("ram")
