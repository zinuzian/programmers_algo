def solution(prices):
    answer = []
    while prices:
        test = prices.pop(0)
        down = False
        for i,val in enumerate(prices):
            if val < test:
                answer.append(i+1)
                down = True
                break
        if not down:
            answer.append(len(prices))


    return answer





print(solution([1, 2, 3, 2, 3]),solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])