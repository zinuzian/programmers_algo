def solution(budgets, M):
    answer = 0

    _min = min(min(budgets), M//len(budgets))
    _max = max(budgets)

    mid = 0
    while _min <= _max:

        mid = (_max + _min) // 2

        s = sum([b if b < mid else mid for b in budgets])

        if s > M:
            _max = mid - 1
        elif s < M:
            _min = mid + 1
        else:
            return mid

    return min(_max, _min)



print(solution([120, 110, 140, 150], 4), solution([120, 110, 140, 150], 4) == 1)