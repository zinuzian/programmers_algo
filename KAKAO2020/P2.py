def solution(p):
    answer = ''
    if not p:
        return answer

    p = list(p)
    u = ""
    zero = 0
    ch = p.pop(0)
    if ch == '(':
        zero += 1
    else:
        zero -= 1
    u += ch
    while zero != 0:
        ch = p.pop(0)
        if ch == '(':
            zero += 1
        else:
            zero -= 1
        u += ch




    if u[0] == '(':
        return u + solution(p)
    else:
        temp = "(" + solution(p) + ")"
        u = u[1:len(u)-1]
        l = len(u)//2
        temp += u[l:] + u[:l]
        return temp


    return answer




print(solution("(()())()"), solution("(()())()") == "(()())()")
print(solution(")("), solution(")(") == "()")
print(solution("()))((()"), solution("()))((()") == "()(())()")