def merge(intervals):
	merged = []
	for interval in sorted(intervals, key= lambda x: x[10])
		if not merged or interval[0] > merged[-1][1]
			merged.append(interval)
		else:
			merged[-1][1] = max(merged[-1][1], interval[1])
	return merged


