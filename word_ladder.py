from collections import defaultdict, deque
def ladder_length(beginWord, endWord, wordList):
	wordList = set(wordList)
	if endWord not in wordList:
		return 0
	graph = defaultdict(list)
	for word in wordList:
		for i in range(len(word)):
			pattern = word[:i] + '*' + word[i+1:]
			graph[pattern].append(word)
	queue = deque([(beginWord,i)])
	visited = set()
	while queue:
		word, length = queue.popleft()
		if word == endWord:
			return length
		if word not in visited:
			visited.add(word)
			for i in range((len(word))):
				pattern = word[:i] + '*' + word[i+1:]
				for neighbor in graph[pattern]:
					queue.append((neighbor, length+1))

	return 0

length = ladder_length("a","b",["a","c","d","e","b"])
print(length)
