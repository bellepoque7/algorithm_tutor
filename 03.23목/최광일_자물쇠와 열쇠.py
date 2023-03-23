'''
스터디 그룹 - 자물쇠와 열쇠

Fail !!!
Rotation까지만 구현

Kye와 Lock을 맞추는 로직 미구현 상태

'''


global N, M,key

def printK(key):
    for i in key:
        print(i)

def rotate90(key):
    # newKey = [[0]*M]*M
    global M, N
    print('** rorate 90 ***')
    M = len(key[0])

    newKey = [[0 for c in range(M)] for r in range(M)]

    for r in range(M):
        for c in range(M):
            newKey[c][M - r - 1] = key[r][c]

    return newKey


def solution(key,lock):
    global N, M

    for _ in range(4):
        key = rotate90(key)
        printK(key)

    answer = True
    return answer


def main():
    global N, M, key

    lock = []
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    M = 3
    # key = [[1,0,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,1]]
    # M = 4

    solution(key,lock)


if __name__ == '__main__':
    main()
