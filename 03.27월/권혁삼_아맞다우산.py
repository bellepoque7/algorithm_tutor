#성공

import sys
from itertools import permutations
from collections import *
import copy
read = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(k):
    global A,V,Q,temp,R,C
    while len(Q)>0:
        r,c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C or A[nr][nc]==7 or V[nr][nc]!=0:
                continue

            V[nr][nc] = V[r][c] + 1
            if A[nr][nc]==k:
                temp.append((nr,nc))
                return V[nr][nc]
            Q.append((nr, nc))

        # for i in range(R):
        #     print(V[i])
        # print()
C,R = map(int,read().split())
A=[[0]*C for _ in range(R)]
B=[[0]*C for _ in range(R)]
s_r,s_c = 0,0
e_r,e_c = 0,0
cnt=1
for i in range(R):
    a = read()
    for j in range(len(a)):

        if a[j]=='#':
            A[i][j]=7
        elif a[j]=='S':
            s_r = i
            s_c = j
        elif a[j]=='E':
            A[i][j] = 8
            e_r = i
            e_c = j
        elif a[j]=='X':
            cnt += 1
            A[i][j]=cnt
# for i in range(R):
#     print(A[i])
# print(cnt)

temp = list(permutations(range(2,cnt+1),cnt-1))
# print(temp)
AAA = 1e9
for condition in temp:
    # map = copy.deepcopy(A)
    Q = deque()
    Q.append((s_r,s_c))
    result = 0
    conditions = []
    for i in condition:
        conditions.append(i)
    conditions.append(8)
    for i in conditions:
        V = copy.deepcopy(B)
        temp = deque()
        result += bfs(i)
        Q = temp
        # print(Q)
        # print(result)
    AAA = min(result,AAA)

print(AAA)
