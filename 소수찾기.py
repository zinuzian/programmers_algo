def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#
#
# import copy
#
#
# def solution(numbers):
#     global answer
#     global primes
#     primes = []
#     answer = 0
#     numbers = list(numbers)
#
#     def dfs(text, lst):
#         global answer
#         if text and int(text) not in primes and is_prime(int(text)):
#             answer += 1
#             primes.append(int(text))
#         if not lst:
#             return
#
#         else:
#
#             for i in range(len(lst)):
#                 temp_text = copy.deepcopy(text)
#                 temp = copy.deepcopy(lst)
#                 i = temp.pop(i)
#                 temp_text += i
#                 dfs(temp_text, temp)
#
#     dfs("", numbers)
#
#     return answer

def solution(numbers):
    answer = 0
    from itertools import permutations
    number_pool = set()

    for i in range(len(numbers)):
        permutations(numbers[:i], i+1)



    return answer


print(solution("17"))
print(solution("011"))