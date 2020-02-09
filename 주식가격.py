def solution(prices):
    answer = [1] * len(prices)
    answer[-1] = 0

    _list = list(reversed(prices))
    _min = 10000

    for idx, val in enumerate(_list):
        if _min >= val:
            answer[idx] = idx
            _min = val

        else:
            if _list[idx - 1] >= val:
                answer[idx] = answer[idx - 1] + 1
            else:
                answer[idx] = 1




    return list(reversed(answer))





print(solution([1, 2, 3, 2, 3]),solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
print(solution([1,4,2,2,1]))