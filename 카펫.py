def solution(brown, red):
    answer = []

    total = brown + red
    col_lst = []
    for i in range(3, int(total**0.5) + 1):
        if total%i == 0:
            col_lst.append(i)




    return answer



print(solution(10,2), solution(10,2) == [4,3])
print(solution(8,1), solution(8,1) == [3,3])
print(solution(24,24), solution(24,24) == [8,6])
