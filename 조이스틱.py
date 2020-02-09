def solution(name):
    answer = 0
    NUM_OF_ALPHABETS = ord('z') - ord('a') + 1
    comp = list('A'*len(name))
    name = list(name)
    idx = 0

    while str(name) != str(comp):
        if name[idx] != 'A':
            if ord(name[idx]) > ord('N'):
                answer += ord('Z') - ord(name[idx]) + 1
                name[idx] = 'A'
            else:
                answer += ord(name[idx]) - ord('A')
                name[idx] = 'A'
        else:
            left = 1
            while name[idx - left] == 'A':
                left += 1
            right = 1
            while name[(idx + right)%len(name)] == 'A':
                right += 1

            if left > right:
                answer += right
                idx += right
                idx %= len(name)
            elif left <= right:
                answer += left
                idx -= left
                if idx < 0:
                    idx += len(name)
            # else:
            #     left = 1
            #     right = 1
            #     while name[idx - left] == 'A':
            #         left += 1
            #     while name[(idx + right) % len(name)] == 'A':
            #         right += 1

    return answer




print(solution("JERAOAAAAEN"))
print(solution("JAN"))
# a0 b1 c2 d3 e4 f5 g6 h7 i8 j9 k10 l11 m12 n13 o12 p11 q10 r9 s8 t7 u6 v5 w4 x3 y2 z1