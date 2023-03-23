def rotate(key):
    # 열쇠를 시계 방향으로 90도 회전하는 함수
    n = len(key)
    new_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[j][n-i-1] = key[i][j]
    return new_key

def check(lock):
    # 자물쇠의 중간 부분이 모두 1인지 확인하는 함수
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 3배로 만들어서 가운데에 두고 시작
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4번 회전시키면서 확인
    for _ in range(4):
        key = rotate(key)
        for i in range(n*2):
            for j in range(n*2):
                # 열쇠를 자물쇠에 삽입
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                # 자물쇠의 중앙 부분이 모두 1이면 True 반환
                if check(new_lock):
                    return True
                # 열쇠를 다시 빼기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
    # 모든 경우를 다 확인한 후에도 자물쇠를 열 수 없으면 False 반환
    return False
