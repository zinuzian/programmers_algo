def solution(a, b):
    #2016/1/1 은 FRI

    answer = ''
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    nod = [31,29,31,30,31,30,31,31,30,31,30,31]
    number = 0
    if a!= 1:
        number += sum(nod[:a-1])
    number += b - 1

    return days[ ( number + 5 ) % 7 ]





print(solution(5,24), solution(5,24) == "TUE")
print(solution(2,18), solution(2,18) == "THU")