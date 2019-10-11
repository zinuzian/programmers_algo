def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i == answer[-1]:
            continue
        else:
            answer.append(i)
    return answer





print(solution([1,1,3,3,0,1,1]), solution([1,1,3,3,0,1,1]) == [1,3,0,1])
print(solution([4,4,4,3,3]), solution([4,4,4,3,3]) == [4,3])
