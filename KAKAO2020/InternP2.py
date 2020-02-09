def solution(p):
    answer = []

    lst = p[2:len(p)-2].split("},{")
    lst = sorted(lst, key=len)

    lst2 = []

    prev = lst[0]
    lst2.append(int(prev))
    for i in lst[1:]:
        lst2.append(
            list(set(map(int, i.split(","))) - set(map(int, prev.split(","))))[0]
        )
        prev = i

    print(lst2)


    # [4, 2, 6, 8]
    return answer





solution("{{2,6,4,8},{4},{4,2},{2,4,6}}")