def solution(priorities, location):
    answer = 0
    found = True
    while found:
        val = priorities[0]
        idx = 0
        if val == max(priorities):
            # pop
            answer += 1
            if idx == location:
                found = False
                break

            del priorities[0]

        else:
            # append
            priorities.append(priorities[0])
            del priorities[0]

        location -= 1
        if location < 0:
            location += len(priorities)
    return answer




print(solution([1, 1, 9, 1, 1, 1],	0))