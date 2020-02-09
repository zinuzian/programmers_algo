def solution(n, edge):
    answer = 0
    UNVISITED = -1

    adj_mat = dict()
    for i in range(n):
        adj_mat[i] = []

    visited = [UNVISITED] * n
    visited[0] = 0
    _max = 0

    for e in edge:
        adj_mat[e[0]-1] += [e[1]-1]
        adj_mat[e[1] - 1] += [e[0] - 1]

    # print(adj_mat)
    q = [[0,0]]

    while q:
        curr = q.pop(0)
        dist = curr[1] + 1

        for idx in adj_mat[curr[0]]:
            if visited[idx] == UNVISITED:
                q.append([idx, dist])
                visited[idx] = dist

    answer = visited.count(max(visited))
    return answer



print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3)