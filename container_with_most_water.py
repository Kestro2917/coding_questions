def max_area(height):
	max_area = 0
	left, right = 0, len(height) - 1
	while left < right:
		max_area = max(max_area, min(height[left], height[right]) * (right - left))
		if height[left] < height[right]:
			left += 1
		else:
			right -= 1
	return max_area

area = max_area("10")
print(area)
