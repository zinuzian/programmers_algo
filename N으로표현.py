def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        # 사용된 숫자는 중복을 없에기 위해 전체 길이의 반까지만 확인
        for x_idx in range(int(i/2)):
            # x는 N이 x_idx+1번 쓰인 경우
            for x in S[x_idx]:
                # y는 N이 i-x_idx-1번 쓰인 경우
                for y in S[i - x_idx - 2]:
                    # x와 y를 이용했기 때문에 전체 N이 i번 쓰인 경우입니다
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if x!=0: case_set.add(y//x)
                    if y!=0: case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
    return -1



print(solution(5,12),solution(5,12)==4)
print(solution(2,11),solution(2,11)==3)
