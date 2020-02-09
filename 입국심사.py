def solution(n, times):
    answer = 0

    _min = 1
    _max = times[0] * n

    while _min < _max:
        mid = (_min + _max) // 2

        max_n = 0
        for i in times:
            max_n += (mid // i)

        if max_n > n:
            _max = mid - 1
        elif max_n < n:
            _min = mid + 1
        else:
            _max = mid
        # print(_min, mid, _max)



    return _min




print(solution(6, [7,10]), solution(6, [7,10]) == 28)