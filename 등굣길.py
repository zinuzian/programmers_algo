def solution(m, n, puddles):
    ways = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        ways[0][i] = 1
    for i in range(n):
        ways[i][0] = 1


    for i in range(1, n):
        for j in range(1, m):
            if [j+1, i+1] in puddles:
                ways[i][j] = 0
            else:
                ways[i][j] = (ways[i - 1][j] + ways[i][j - 1])


    return ways[n-1][m-1]  % 1000000007




print(solution(4,3,[[2, 2]]),solution(4,3,[[2, 2]]) == 4)