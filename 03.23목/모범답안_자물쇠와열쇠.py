def rotate_90(a):
    n = len(a) # 행길이
    m = len(a[0]) # 열길이
    result = [[0]*n for _ in range(m)] # 90도 회전 결과 담을 리스트
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j] # 로직이 떠오르지 않았으면 임의로 만들어서 테스트
    
    # print('--- 열쇠 90도 잘돌아가는지 확인----')
    # for i in range(n):
    #     print(result[i])
    return result

#확장된 자물쇠의 중간부분이 모두 1인지 확인
#기둥과 보 possible 함수처럼 기저조건을 True로, 하나라도 잘못된게 발견되면 바로 return False
def check(lock_3x):
    lock_length = len(lock_3x) //3 # 3
    for i in range(lock_length, lock_length*2): # 3,4,5
        for j in range(lock_length, lock_length*2): #3,4,5
            if lock_3x[i][j] !=1 : # 하나라도 정확히 1이 아니면 맞지 열쇠가 맞지 않는것
                return False
    #기저조건 True
    return True 


def solution(key,lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 3배로 변환
    lock_3x = [[0]* (n*3) for _ in range(n*3)]
    # 3배로 만든 자물쇠에 중앙 부분의 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            lock_3x[i+n][j+n] = lock[i][j]
    # print('--- 열쇠 확인 ----')
    # for i in range(n):
    #     print(key[i])
    # print('--- 자물쇠 확인 ----')
    # for i in range(n):
    #     print(lock[i])
    # print('--- 자물쇠 3배로 만들기 ----')
    # for i in range(n*3):
    #     print(lock_3x[i])

    #확인하는 단계, 4가지 방향에 대해 모두 확인해야하므로 
    for _ in range(4):
        key = rotate_90(key) #열쇠 회전
        #열쇠넣을 좌측상단 정하기 (0,0)부터 (6,6)까지!
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠 넣기, 하기 루프 2개가 열쇠 9칸 수행하는 1묶음
                for i in range(m):
                    for j in range(m):
                        lock_3x[x+i][y+j] += key[i][j]   #x+i의 최소값 0 최대값 3n, y+j도 동일
                        # for k in range(n*3):
                        #     print(lock_3x[k])
                        # print('-----')
                # 새로운 자물쇠에 열쇠가 맞는지 check 함수로 검사
                if check(lock_3x) == True:
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        lock_3x[x+i][y+j] -= key[i][j]
    # 4가지 모두 안맞는다면 기저조건 False
    return False

solution(key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]])