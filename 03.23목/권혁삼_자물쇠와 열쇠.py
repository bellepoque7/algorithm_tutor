#61점

#90도 회전 함수
def ro_90(A):
    global M
    l = len(A)
    B =[[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            B[j][l-1-i] = A[i][j]
        
    return B 

def bigger(A):
    global M
    l = len(A)
    B =[[0]*M for _ in range(M)]
    for i in range(l):
        if i>M-1:
            break
        for j in range(l):
            if j>M-1:
                break
            B[i][j] = A[i][j]
    return B 

# 시작 위치 변경
def move(A,B):
    global M
    r,c = B
    l = len(A)
    C =[[0]*M for _ in range(M)]
    for i in range(l):
        if i+r>M-1:
            break
        for j in range(l):
            if j+c>M-1:
                break
            C[i+r][j+c] = A[i][j]
    return C 


def solution(key, lock):
    global M
    answer = False
    N = len(key)
    M = len(lock)
    A = key
    for a in range(4):
        
        key_rot = ro_90(A)
        A = key_rot
        #scale 확장
        key_big = bigger(A)
        for b in range(M):
            for c in range(M):
                D = key_big
                key_move = move(D,(b,c))
                flag = True
                for i in range(M):
                    if flag == False:
                        break
                    for j in range(M):
                        if lock[i][j]+key_move[i][j]==0:
                            flag = False
                            break
                        elif lock[i][j]+key_move[i][j]==2:
                            flag = False
                            break
                if flag:
                    answer=True
        
    return answer
