''' 아맞다우산 
튜터님 틀린곳좀 찾아주세요... 예제답도 나와서..'''

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import *
from itertools import *

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(idx,r,c):
    Q = deque()
    Q.append((r,c))
    visited = [[0]*N for _ in range(M)]
    visited[r][c] = 1
    # print(Q)
    while len(Q)>0:
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr<0 or nr>=M or nc<0 or nc>=N or a[nr][nc]=='#' or visited[nr][nc]!=0:
                continue
            if a[nr][nc] == 'S' or a[nr][nc] == 'X' or a[nr][nc] == 'E':
                distance[idx][check.index((nr,nc))] = visited[r][c]
            
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr,nc))

N, M = map(int,read().rsplit())


a = [list(read().rstrip()) for _ in range(M)]

check = []
for i in range(M):
    for j in range(N):
        if a[i][j] == 'S':
            check.append((i,j))
        if a[i][j] == 'X':
            check.append((i,j))
        if a[i][j] == 'E':
            check.append((i,j))
# S,E를 구분없이 넣었음 괜찮을까?..
# print(check)
distance = [[0] * len(check) for _ in range(len(check))]
# print('distance',distance)
index_check = []
for idx, v in enumerate(check): 
    index_check.append(idx)
    bfs(idx,v[0],v[1])
# for i in range(M):
#     print(distance[i])

# res = 1e9
res = []
for permu in permutations(index_check):
    # print(permu)
    new = [0] + list(permu) + [len(check)-1]
    print(new,) # [0, 0, 1, 2, 3, 4, 5, 5] 양 끝 0,5를 제외하고 순열조합 
    temp = 0
    for i in range(len(new)-1):
        temp += distance[new[i]][new[i+1]]
    # print(temp)
    # res = min(res, temp)
    res.append(temp)
# print(res)
# print(min(res))