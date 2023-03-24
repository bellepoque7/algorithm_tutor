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
    for i in range(len(key)):
        print(a[i])
    print('-----')
    b = rotate90(a) #90도
    for i in range(len(key)):
        print(b[i])
    print('-----')
    c = rotate90(b) #180도
    for i in range(len(key)):
        print(c[i])
    print('-----')
    d = rotate90(c) #270도
    for i in range(len(key)):
        print(d[i])
    print('-----')
    if a or b or c or d in lock:
        return True

solution(key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]])