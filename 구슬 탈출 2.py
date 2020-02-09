class INFO:
    def __init__(self, rx, ry, bx, by, cnt):
        self.rx = rx
        self.ry = ry
        self.bx = bx
        self.by = by
        self.cnt = cnt


def solution(N, M, board):
    move_y = [1, 0, -1, 0]
    move_x = [0, 1, 0, -1]

    def bfs(start):
        queue = [start]
        visited = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
        visited[start.ry][start.rx][start.by][start.bx] = True
        answer = -1

        while queue:
            now = queue.pop(0)
            if now.cnt > 10:
                break
            if board[now.ry][now.rx] == "O" and board[now.by][now.bx] != "O":
                answer = now.cnt
                break

            for i in range(4):
                next_rx = now.rx
                next_ry = now.ry
                next_bx = now.bx
                next_by = now.by

                # move red
                cnt_r = 0
                while board[next_ry][next_rx] not in "#O":
                    next_rx += move_x[i]
                    next_ry += move_y[i]
                    cnt_r += 1

                if board[next_ry][next_rx] == "#":
                    next_rx -= move_x[i]
                    next_ry -= move_y[i]
                    cnt_r -= 1

                # move blue
                cnt_b = 0
                while board[next_by][next_bx] not in "#O":
                    next_bx += move_x[i]
                    next_by += move_y[i]
                    cnt_b += 1

                if board[next_by][next_bx] == "#":
                    next_bx -= move_x[i]
                    next_by -= move_y[i]
                    cnt_b -= 1

                if next_rx == next_bx and next_ry == next_by:
                    if board[next_ry][next_rx] != "O":
                        if cnt_b > cnt_r:
                            next_bx -= move_x[i]
                            next_by -= move_y[i]
                        else:
                            next_rx -= move_x[i]
                            next_ry -= move_y[i]

                if not visited[next_ry][next_rx][next_by][next_bx]:
                    visited[next_ry][next_rx][next_by][next_bx] = True
                    next = INFO(next_rx, next_ry, next_bx, next_by, now.cnt+1)
                    queue.append(next)

        return answer

    pos_rx = 0
    pos_ry = 0
    pos_bx = 0
    pos_by = 0

    # find  R, B
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                pos_rx = j
                pos_ry = i
            elif board[i][j] == 'B':
                pos_bx = j
                pos_by = i
    start = INFO(pos_rx, pos_ry, pos_bx, pos_by, 0)
    return bfs(start)


N, M = map(int, input().split(" "))
board = []
for i in range(N):
    board.append(input())

print(solution(N, M, board))
