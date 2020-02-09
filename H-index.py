def solution(citations):
    answer = 0
    for i, v in enumerate(sorted(citations, reverse=True)):
        if v-1 < i:
            return answer
        else:
            answer += 1
    return answer



print(solution([3, 0, 6, 1, 5]), solution([3, 0, 6, 1, 5]) == 3)