import copy
route = []
def solution(tickets):
    global route

    def dfs(rt, lst):
        global route
        if len(lst) == 0:
            route.append(rt)

        i = 0
        while i < len(lst):
            if lst[i][0] == rt[-1]:
                c = copy.deepcopy(lst)
                c.pop(i)
                dfs(rt + [lst[i][1]], c)
            i += 1



    dfs(["ICN"], tickets)

    route = sorted(route, key=lambda x:"".join(x))
    answer = route[0]
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))