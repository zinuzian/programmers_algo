import heapq


def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs = sorted(jobs, key=lambda x:x[0])
    heap = []
    p = 0


    while jobs or heap:

        if jobs and not heap and jobs[0][0] >= p:
            p = jobs[0][0]

        while jobs and jobs[0][0] <= p:
            job = jobs.pop(0)
            heapq.heappush(heap, (job[1], job[0]))

        c, s = heapq.heappop(heap)
        answer += p-s + c
        p += c
    return answer//n



print(solution([[0, 3], [1, 9], [2, 6]]), solution([[0, 3], [1, 9], [2, 6]]) == 9)