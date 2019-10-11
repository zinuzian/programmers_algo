def solution(skill, skill_trees):
    answer = 0
    import re
    pattern = re.sub("["+skill+"]","","[ABCDEFGHIJKLMNOPQRSTUVWXYZ]")
    if pattern == "[]":
        pattern = ""
    for i,val in enumerate(skill_trees):
        skill_trees[i] = re.sub(pattern,"",val)


    for i in skill_trees:
        if i == "":
            answer += 1
        elif i[0] == skill[0] and skill.find(i) != -1:
            answer += 1




    return answer





print(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ",["BACDE", "CBADF", "AECB", "BDA"]),solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])==2)
