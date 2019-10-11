
fibonacci = [0]


def fibo(num):
    global fibonacci
    if num == 0 or num == 1:
        return fibonacci[num]
    else:
        if fibonacci[num - 1] != 0 and fibonacci[num - 2] != 0:
            fibonacci[num] = fibonacci[num - 1] + fibonacci[num - 2]
            return fibonacci[num]
        else:
            fibonacci[num] = fibo(num - 1) + fibo(num - 2)
            return fibonacci[num]

def solution(N):
    global fibonacci
    fibonacci = [1,1] + [0] * N

    answer = 4 * fibo(N-1) + 2 * fibo(N-2)


    return answer





print(solution(5), solution(5) == 26)
print(solution(6), solution(6) == 42)




