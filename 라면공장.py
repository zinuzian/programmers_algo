def solution(stock, dates, supplies, k):
    import heapq
    answer = 0
    last_day = -1
    cand = []
    while stock < k:
        for i in range(last_day + 1, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(cand, -supplies[i])
                last_day = i
            else:
                break

        stock -= heapq.heappop(cand)
        answer += 1

    return answer




print(solution(4, [4,10,15], [20,5,10], 30), solution(4, [4,10,15], [20,5,10], 30) == 2)