'''73점, 배열 크기다를 경우 진행해야함'''

def rotate90(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = arr[len(arr)-1-j][i]
    return arr

def solution(key, lock): # 0 홈 , 1 돌기

    # key를 반전 시킴 (맞는 자물쇠 찾기 위해)
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                key[i][j] = 0
            else :
                key[i][j] = 1
    # print(key)
    a = key
    b = rotate90(a) #90도
    c = rotate90(b) #180도
    d = rotate90(c) #270도
    
    if a or b or c or d in lock:
        return True
    return False
