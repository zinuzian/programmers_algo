def solution(heights):
    answer = []

    _stack = []

    for i, val in enumerate(heights):
        _stack.insert(0, heights.pop())

        if max(heights) <= _stack[0]:
            answer.insert(0,0)

        else:







    return answer






a = solution([6,9,5,7,4])
print(a, a == [0,0,2,2,4])

a = solution([3,9,9,3,5,7,2])
print(a, a == [0,0,0,3,3,3,6])

a = solution([1,5,3,6,7,6,5])
print(a, a == [0,0,2,0,0,5,6])


