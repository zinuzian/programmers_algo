def solution(progresses, speeds):
    answer = []
    import math
    while len(progresses) != 0:
        needed_loop = math.ceil((100 - progresses[0]) / speeds[0])
        for idx, val in enumerate(speeds):
            progresses[idx] += val * needed_loop
            if progresses[idx] > 100:
                progresses[idx] = 100
        done = 0
        for i, val in enumerate(progresses):
            if val==100:
                if i == 0:
                    done += 1
                elif progresses[i-1] == 100:
                    done += 1
                else:
                    break

        answer.append(done)
        progresses = progresses[done:]
        speeds = speeds[done:]

    return answer



print(solution([93,10,55], [3,30,5]),solution([93,30,55], [1,30,5]) == [2,1])


string = "hello"
print(list(string))













