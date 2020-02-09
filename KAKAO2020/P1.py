

def solution(s):
    answer = 1000
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        loc_min = 1000
        pattern = s[:i]
        cnt = 1
        rst = ""
        for j in range(i, len(s), i):

            if s[j:j+i] == pattern:
                cnt += 1
            else:
                if cnt == 1:
                    rst += pattern
                else:
                    rst += str(cnt) + pattern
                pattern = s[j:j+i]
                cnt = 1
        if cnt == 1:
            rst += pattern
        else:
            rst += pattern + str(cnt)

        loc_min = len(rst)

        if answer > loc_min:
            answer = loc_min
    return answer








print(solution("aabbaccc"), solution("aabbaccc") == 7)
print(solution("ababcdcdababcdcd"), solution("ababcdcdababcdcd") == 9)
print(solution("abcabcdede"), solution("abcabcdede") == 8)
print(solution("abcabcabcabcdededededede"), solution("abcabcabcabcdededededede") == 14)
print(solution("xababcdcdababcdcd"), solution("xababcdcdababcdcd") == 17)
