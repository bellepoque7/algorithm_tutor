# 못풀었습니다, 73점?
# 같은 모양일때만 구현..

def rotate90(arr):
    
    v = [[0] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            v[i][j] = arr[j][len(arr)-1-i]
    return v

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
    print(a)
    b = rotate90(a) #90도
    print(b)
    c = rotate90(b) #180도
    print(c)
    d = rotate90(c) #270도
    print(d)
    if a or b or c or d in lock:
        return True
