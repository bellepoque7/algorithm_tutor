## pass 772

from collections import deque
from itertools import *
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global start, end, items, item_permu, a, visited
    Q = deque()
    Q_item = deque() 
    res = []
       
    for item in item_permu:
        for i in item:
            Q_item.append(i)
        Q_item.append(end)
        # print(Q_item)

        cnt = 0
        Q.clear()

        Q.append(start)
        visited[start[0]][start[1]] = 1

        while Q_item:
            x, y = Q_item.popleft()

            while Q:
                r, c = Q.popleft()
                
                if r == x and c == y: # 순열 아이템 값을 만나면 큐 초기화 하고, 아이템 위치 append
                    cnt += visited[r][c] - 1
                    # print(f'cnt {cnt}')
                    Q.clear()
                    visited = [[0 for _ in range(C)] for _ in range(R)]

                    Q.append((x, y))
                    break

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        continue

                    if visited[nr][nc] != 0 or a[nr][nc] == '#':
                        continue
                    
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1


                # for i in range(R):
                #     for j in range(C):
                #         print(visited[i][j], end = ' ')
                #     print()
                # print('==========================')

            visited = [[0 for _ in range(C)] for _ in range(R)]
            visited[x][y] = 1
            # tmp = input()
        res.append(cnt)
        # print(res)


    return min(res)


C, R = map(int, input().split())
a = []
for i in range(R):
    a.append(list(map(str, input())))
visited = [[0 for _ in range(C)] for _ in range(R)]

start = ()
end = ()
items = []
for i in range(R):
    for j in range(C):
        if a[i][j] == 'S':
            start = (i, j)
        elif a[i][j] == 'X':
            items.append((i, j))
        elif a[i][j] == 'E':
            end = (i, j)

item_permu = list(permutations(items, len(items)))


print(bfs())
