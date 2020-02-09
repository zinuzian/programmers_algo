def solution(m, n, puddles):
    ways = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(m+1):
        ways[1][i] = 1
    for i in range(n+1):
        ways[i][1] = 1
    for x, y in puddles:
        ways[y][x] = 0

    for i in range(2, n+1):
        for j in range(2, m+1):
            ways[i][j] = (ways[i - 1][j] + ways[i][j - 1])


    return ways[n][m]  % 1000000007




print(solution(4,3,[[2, 2]]),solution(4,3,[[2, 2]]) == 4)


def solution(m, n, puddles):
    # 지도
    grid = [[0] * (m + 1) for _ in range(n + 1)]

    # 물에 잠긴 지역
    for x, y in puddles:
        grid[y][x] = -1

    # 집
    grid[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] == -1:
                grid[i][j] = 0
                continue
            if grid[i - 1][j] > 0:
                grid[i][j] += grid[i - 1][j]
            if grid[i][j - 1] > 0:
                grid[i][j] += grid[i][j - 1]

    return grid[n][m] % 1000000007