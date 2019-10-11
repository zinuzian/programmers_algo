def solution(s):
    n = len(s)
    if n % 2 == 0:
        return s[n//2-1:n//2+1]
    else:
        return s[n//2]






print(solution("abcde"),solution("abcde") == "c")
print(solution("qwer"),	solution("qwer")=="we")