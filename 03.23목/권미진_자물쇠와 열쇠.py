#미완성

def dfs(r,c):
    
def rotate_90(A,N):
    temp = [[0]*N for _ in range()]
    for i in range(N):
        for j in range(N):
            temp[i][j] = a[N-j-1][i]
        return temp


def solution(key, lock):
    M = len(key)
    N = len(lock)
    flag = 0
    for i in range(3):
        if flag:
            rotate_90(key,M)
            flag = 1
            
        key_list = []
        for r in range(M):
            for c in range(M):
                if key[r][c] == 1:
                    key_list.append((r,c))

    answer = True
    return answer
