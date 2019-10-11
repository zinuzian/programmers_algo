def solution(bridge_length, weight, truck_weights):
    answer = 0

    b = [0]*bridge_length
    truck_weights = sorted(truck_weights,reverse=True)

    while b:
        b.pop(0)
        answer += 1
        if truck_weights:
            if sum(b) + truck_weights[0] <= weight:
                b.append(truck_weights[0])
                del truck_weights[0]
            else:
                b.append(0)






    return answer




print(solution(2,10,[7,4,5,6]), solution(2,10,[7,4,5,6]) == 8)
print(solution(100,100,[10]), solution(100,100,[10]) == 101)
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]), solution(100,100,[10,10,10,10,10,10,10,10,10,10]) == 110)


