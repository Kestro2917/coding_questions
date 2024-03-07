def two_sum(nums, target):
	num_dict = {}
	for i, num in enumerate(nums):
		complement = target - num
		if complement in num_dict:
			return [num_dict[complement],i]
		num_dict[num]= i
	return None

two_sum([2,3,4,8], 8)
