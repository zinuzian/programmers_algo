def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks)

    _min = 1
    _max = distance // (len(rocks) - n) + 1

    while _min < _max:
        mid = (_min + _max) // 2

        dist = [0] * len(rocks) + 1
        for i in range(1, len(rocks)):
            dist




    return answer