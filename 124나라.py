def solution(n):
    answer = ''
    radix = ["1", "2", "4"]

    while True:
        n -= 1
        answer = radix[(n)%3] + answer
        n = n // 3

        if n == 0:
            break

    return answer





print(solution(1), solution(1) == "1")
print(solution(2), solution(2) == "2")
print(solution(3), solution(3) == "4")
print(solution(4), solution(4) == "11")
