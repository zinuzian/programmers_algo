import heapq

heap = [4,1,9,6]

# print(heap[0])


heap=[]
heapq.heappush(heap , (-4, 4))
print(heap)
heapq.heappush(heap , 1)
print(heap)
heapq.heappush(heap , 9)
print(heap)
heapq.heappush(heap , 6)
print(heap)

# print(heap[0][1])
# print(heapq.heappop(heap))
# print(heap[0])
