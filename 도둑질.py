def solution(money):
    answer = 0
    numOfHouse = len(money)
    dp0 = [money[0]] * numOfHouse
    dp1 = [money[1]] * numOfHouse
    dp1[0] = 0

    for i in range(2, numOfHouse - 1):
        dp0[i] = max(dp0[i - 2] + money[i], dp0[i - 1])
        # print(dp0[i], end = ' ')

    # print()

    for i in range(2, numOfHouse):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])
        # print(dp1[i], end = ' ')
    # print()
    return max(dp0[-2], dp1[-1])



print(solution([1,1, 9, 1, 9]))