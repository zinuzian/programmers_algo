def solution(w, h):
    answer = 0
    grad = (h / w)
    a = w
    b = h
    if w < h:
        a, b = b, a

    while b != 0:
        n = a % b
        a = b
        b = n

    for x in range(w // a):
        answer += int(grad * x)

    return 2* (answer * a + sum(range(a))*
               (w//a)*
               (h//a))



print(solution(8,12))