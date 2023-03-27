
3월27일 오후2시 - 현재까지 모르겠음
생각한 것
'X'를 만나면 'S'로 바꾸고 visited초기화
'X'를 만날때까지 bfs돌고 함수를 끝냄


import sys
from heapq import *
from collections import deque
from itertools import *

read = sys.stdin.readline

global n, m, arr, visited, cnt


def bfs(r, c):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    cnt = 0

    while len(q) > 0:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if arr[nr][nc] == 'E' :
                return cnt

            elif arr[nr][nc] == 'X' :
                arr[nr][nc] == 'S'
                cnt +=1
                return

            if arr[nr][nc] == '#' or visited[nr][nc] != 0 :
                continue
            elif arr[nr][nc] == '.' :
                q.append((nr,nc))
                visited[nr][nc] = 1
                cnt += 1



def main():
    global n, m, arr, visited, cnt

    m, n = map(int, read().split())
    arr = []
    cnt = 0
    visited = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        arr.append(list(read().rstrip()))
        num_X = arr[i].count('X')

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'S':
                bfs(i, j)
                visited = [[0 for i in range(m)] for j in range(n)]

    print(cnt)
if __name__ == '__main__':
    main()
