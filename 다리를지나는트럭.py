def solution(bridge_length, weight, truck_weights):
    answer = 1
    onload = truck_weights[0]
    b = [0]*(bridge_length-1) +[truck_weights.pop(0)]
    # truck_weights = sorted(truck_weights,reverse=True)
    print(b)
    while truck_weights:
        if onload + truck_weights[0] > weight:
            i = 0
            while b[i] == 0:
                i+=1
            onload -= b[i]
            b = b[i+1:] + [0]*(i+1)
            print(b, onload)
            answer += i+1

        else:
            t = b.pop(0)
            onload -= t
            b.append(truck_weights.pop(0))
            print(b)
            answer += 1

    answer += bridge_length


    return answer




print(solution(2,10,[7,4,5,6]), solution(2,10,[7,4,5,6]) == 8)
print(solution(100,100,[10]), solution(100,100,[10]) == 101)
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]), solution(100,100,[10,10,10,10,10,10,10,10,10,10]) == 110)


