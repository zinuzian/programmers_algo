def solution(triangle):
    answer = 0
    answer = max(dp(triangle))
    return answer

ret_tri = []


def dp(triangle):
    global  ret_tri
    n = len(triangle)
    ret = [0] * n
    if n == 1:
        ret_tri.append([triangle[0][0]])
        return [triangle[0][0]]
    else:
        if len(ret_tri) != n-1:
            ret[0] = dp(triangle[:n-1])[0] + triangle[n-1][0]
        else:
            ret[0] = ret_tri[n-2][0] + triangle[n-2][0]
        for i in range(1,n-1):
            ret[i] = max(ret_tri[n-2][i-1], ret_tri[n-2][i]) + triangle[n-1][i]
        ret[n-1] = ret_tri[n-2][-1] + triangle[n-1][n-1]
    ret_tri.append(ret)
    return ret





print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]),solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30)