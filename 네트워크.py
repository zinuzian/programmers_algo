def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]


    while computers:
        queue = []
        for i in range(n):
            if not visited[i]:
                queue.append(i)
                break

        if len(queue) == 0:
            break

        answer += 1
        while queue:
            next_computer = queue.pop(0)
            neighbors = computers[next_computer]
            for i, val in enumerate(neighbors):
                if val == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)