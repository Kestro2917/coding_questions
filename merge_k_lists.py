import heapq

def merge_k_lists(lists):
	min_heap = []
	for i, l in enumerate(lists):
		if l:
			heapq.heappush(min_heap, (l.val, i , l))
	dummy = ListNode(0)
	current = dummy
	while min_heap:
		val, i, node = heapq.heappop(min_heap)
		current.next = node
		current = current.next
		if node.next:
			heapq.heappush(min_heap, (node.next.val, i, node.next))
	return dummy.next
