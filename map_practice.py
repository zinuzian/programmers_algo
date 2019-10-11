def solution(numbers):
    answer = ''
    temp = [str(i) for i in numbers]

    answer = "".join(sorted(temp, key=lambda x: x * 3, reverse=True))
    return answer




print(solution([0, 0, 0, 0]))

