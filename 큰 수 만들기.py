def solution(number, k):
    # answer = ''
    # popped = 0
    # idx = 1
    # stack = [number[0]]
    # while popped != k:
    #     if number[idx - 1] < number[idx]:
    #         tmp = 0
    #         while stack and popped < k and number[idx] > stack[-1]:
    #             stack.pop(-1)
    #             tmp += 1
    #             popped += 1
    #
    #         number = number[:idx - tmp] + number[idx:]
    #         idx = 1
    #         stack.append(number[0])
    #
    #     else:
    #         stack.append(number[idx])
    #         idx += 1
    #
    # return number

    # answer = ''
    # popped = 0
    # stack = []
    # for i, num in enumerate(number):
    #     while stack and stack[-1] < num and k > popped:
    #         stack.pop()
    #         popped += 1
    #     if popped == k:
    #         stack += list(number[i:])
    #         break
    #     stack.append(num)
    # stack = stack[:-(k - popped)] if k > popped else stack
    # answer = ''.join(stack)
    # return answer

    while k != 0:
        idx = 0
        while idx < len(number) - 1 and number[idx] >= number[idx+1]:
            idx += 1

        if idx == len(number) - 1:
            return number[:-k]


        if number[idx] < number[idx+1]:
            number = number[:idx] + number[idx+1:]
            k -= 1

    return number




print(solution("1924", 2), solution("1924", 2) == "94")
print(solution("1231234", 3), solution("1231234", 3) == "3234")
print(solution("4177252841", 4), solution("4177252841", 4) == "775841")
print(solution("654321", 2), solution("654321", 2) == "6543")