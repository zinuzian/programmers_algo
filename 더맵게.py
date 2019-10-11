def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville,new)

        answer += 1

    return answer




print(solution([1, 2, 3, 9, 10, 12], 7), solution([1, 2, 3, 9, 10, 12], 7) == 2)