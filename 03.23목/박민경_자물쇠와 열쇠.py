# 현재 54점 

def rotate_right(arr, M):
    tmp = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            tmp[i][j] = arr[M-j-1][i]
    return tmp

def combi(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def delete(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def check_board(N, M, board):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True
    
    
def solution(key, lock):
    N = len(lock)
    M = len(key)
    K = N + M*2 # 자물쇠를 중앙에 올려놓은 새로운 보드 size
    board = [[0 for _ in range(K)] for _ in range(K)]

    #board 가운데 넣기
    for i in range(N):
        for j in range(N):
            board[i+M][j+M] = lock[i][j]

    #key 회전하며 비교
    for i in range(4):
        rotate_key = rotate_right(key, M)

        for start_i in range(N+M):
            for start_j in range(N+M):
                combi(start_i, start_j, M, rotate_key, board)

                if check_board(N, M, board):
                    return True

                delete(start_i, start_j, M, rotate_key, board)
                
    return False
    
