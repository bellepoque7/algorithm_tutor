## 미완성. 한번 지나간 X를 또 지나갈때, count를 하지 않는 로직을 못 세움

from collections import deque


def finding_start_location():
    global area,C,R
    for i in range(R):
        for j in range(C):
            if area[i][j] == 'S':
                S_row = i
                S_col = j
            if area[i][j] == 'E':
                E_row = i
                E_col = j

    return S_row,S_col,E_row,E_col

def count_X():
    global area, C, R
    X_count=0
    for i in range(R):
        for j in range(C):
            if area[i][j] == 'X':
                X_count+=1
    return X_count

C,R = map(int,input().split())

area = [list(input()) for _ in range(R)]

S_row,S_col,E_row,E_col = finding_start_location()
area[S_row][S_col] = "."
area[E_row][E_col] = "."
X_count = count_X()

visit =[[[0] * (X_count+1) for _ in range(C)] for _ in range(R)]


def bfs(r,c,z):
    global R,C,visit,area,X_count
    qu=deque([(r,c,z)])
    while qu:
        r,c,z = qu.popleft()

        if r == E_row and c== E_col and z == X_count:
            return visit[r][c][z]
        # print(f'r:{r} c:{c} z:{z}')
        # print(qu)
        # if r == E_row and c == E_col and z == X_count+1:
        #     print('Done')
        #     return visit[r][c][z]

        for nr,nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
            # print(f'nr:{nr} nc:{nc} z:{z}')
            # print(f'area:{area[nr][nc]} visit[nr][nc][z]:{visit[nr][nc][z]}')
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                # print(f'OutRange case | nr:{nr} nc:{nc} z:{z}')
                continue
            if area[nr][nc] == "#":
                # print(f'# case | nr:{nr} nc:{nc} z:{z}')
                continue
            elif area[nr][nc] == "." and visit[nr][nc][z] == 0:
                # print('Case point')
                visit[nr][nc][z] = visit[r][c][z] + 1
                qu.append((nr,nc,z))
            elif z < X_count and area[nr][nc] == "X" and visit[nr][nc][z] == 0 and visit[nr][nc][z+1]==0:
                # print('Case meet X')

                visit[nr][nc][z+1] = visit[r][c][z] + 1
                qu.append((nr,nc,z+1))


            for i in visit:
                print(i)
            print('----------------------')

result=bfs(S_row,S_col,0)
print(result)
