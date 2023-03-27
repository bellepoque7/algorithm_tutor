import sys
from collections import deque

def bfs(y, x):
    global answer
    q = deque()
    q.append([y, x, 0, 0])
    visited[y][x][0] = 1

    while q:
        y, x, bit, d = q.popleft()

        # d가 현재 최솟값보다 크다면, 그 이상 탐색하지 않아도 됨
        if d < answer:
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]

                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx][bit]:
                    visited[ny][nx][bit] = 1
                    nd = d + 1
                    if board[ny][nx] != '#':
                        # 탈줄점에 도착하고, 모든 물건을 가진 상태일 때
                        if board[ny][nx] == 'E' and bit+1 == 1 << len(pos_things):
                            answer = min(answer, nd)

                        # X를 만나면, 물건을 가진 상태로 변경
                        elif board[ny][nx] == 'X':
                            pos = pos_things.index([ny, nx])
                            nbit = bit | (1 << pos)
                            # print(nbit)
                            visited[ny][nx][nbit] = 1
                            q.append([ny, nx, nbit, nd])

                        else:   # 벽을 만난 경우
                            q.append([ny, nx, bit, nd])


if __name__ == "__main__":
    m, n = map(int, input().split())
    board = []
    # visited[y][x][bit] 물건이 총 5개 이므로 32개
    visited = [[[0 for _ in range(32)] for _ in range(m)] for _ in range(n)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    pos_things = []     # 물건의 위치 저장
    sy, sx = -1, -1
    answer = float('inf')

    for i in range(n):
        tmp = input()
        for j in range(m):
            if tmp[j] == 'S':
                sy, sx = i, j
            elif tmp[j] == 'X':
                pos_things.append([i, j])
        board.append(list(tmp))

    bfs(sy, sx)
    print(answer)