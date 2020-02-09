def solution(begin, target, words):
    answer = 0

    queue = [[begin, 0, [False]*len(words)]]
    _len = len(begin)

    while queue:
        curr = queue.pop(0)
        if curr[0] == target:
            answer = curr[1]
            break
        for word in words:
            used = curr[2].copy()
            if used[words.index(word)]:
                continue
            _sum = 0
            for i in range(_len):
                if word[i] != curr[0][i]:
                    _sum += 1
            if _sum == 1:
                used[words.index(word)] = True
                queue.append([word, curr[1] + 1, used])

    return answer



print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"]), solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"]) == 4)

