from itertools import permutations

def solution(baseball):
    answer = 0
    perms = ["".join(list(s)) for s in list(permutations(['1','2','3','4','5','6','7','8','9'], 3))]
    # print(perms)

    for cand in perms:
        flag = True
        for i in baseball:
            strike = 0
            ball = 0
            item = str(i[0])

            for j in range(len(item)):
                if item[j] == cand[j]:
                    strike += 1
            if i[1] != strike:
                flag = False
                break

            ball = len(set(item) & set(cand))
            ball -= strike
            if ball != i[2]:
                flag = False
                break

        if flag:
            answer += 1


    return answer




print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]), solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]) == 2)