global_max = 0

def solution(N, board):


    def rotate(board):
        new_board = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                new_board[j][N-1-i] = board[i][j]

        return new_board

    def move(board):
        for y in range(N):
            temp = []
            for x in range(N):
                if board[y][x] == 0:
                    temp.append(board[y].pop(x))

        for y in range(N):
            for x in range(1, N):
                if board[y][x] == board[y][x-1]:
                    board[y][x-1] *= 2
                    board[y].pop(x)
                    board[y].append(0)

        return board



    def dfs(board, count):
        global global_max

        if count > 5:
            local_max = 0
            for i in range(N):
                for j in range(N):
                    if local_max < board[i][j]:
                        local_max = board[i][j]
            if local_max > global_max:
                global_max = local_max
            return

        for i in range(4):
            new_board = move(board)
            dfs(new_board, count + 1)
            board = rotate(board)

    return dfs(board, 0)





N = int(input().split(" ")[0])
board = []
for i in range(N):
    board.append(list(map(int, input().split(" "))))
solution(N, board)
print(global_max)