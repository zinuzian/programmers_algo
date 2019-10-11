def solution(arrangement):
    answer = 0
    level = 0
    iterate = iter(range(len(arrangement)))
    for i in iterate:
        if arrangement[i] == '(':
            if arrangement[i+1] == ')':
                #laser
                answer += level
                next(iterate)
            else:
                level += 1
        elif arrangement[i] == ')':
            level -= 1
            answer += 1



    return answer




print(solution("()(((()())(())()))(())"),solution("()(((()())(())()))(())") == 17)