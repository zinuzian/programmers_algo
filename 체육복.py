def solution(n, lost, reserve):
    answer = 0
    avail = [1 for _ in range(n)]
    for idx, val in enumerate(reserve):
        avail[val - 1] += 1
    for idx, val in enumerate(lost):
        avail[val - 1] -= 1

    for idx, val in enumerate(avail):
        if idx != 0:
            if val == 2 and avail[idx-1] == 0:
                avail[idx] -= 1
                avail[idx - 1] += 1
                continue


        if idx != n-1:
            if val == 2 and avail[idx+1] == 0:
                avail[idx] -= 1
                avail[idx + 1] += 1


    for i in avail:
        if i>0:
            answer += 1

    avail = [1 for _ in range(n)]
    for idx, val in enumerate(reserve):
        avail[val - 1] += 1
    for idx, val in enumerate(lost):
        avail[val - 1] -= 1

    for idx, val in enumerate(avail):
        if idx != n - 1:
            if val == 2 and avail[idx + 1] == 0:
                avail[idx] -= 1
                avail[idx + 1] += 1
                continue
        if idx != 0:
            if val == 2 and avail[idx - 1] == 0:
                avail[idx] -= 1
                avail[idx - 1] += 1
    answer2 = 0
    for i in avail:
        if i > 0:
            answer2 += 1

    if answer > answer2:
        return answer
    else:
        return answer2







print(solution(9,[2,4,7,8],[3,6,9]),solution(9,[2,4,7,8],[3,6,9]) == 8)
print(solution(5,[2,4],[3,5]),solution(5,[2,4],[3,5])==5)
print(solution(3,[3],[1]),solution(3,[3],[1])==2)