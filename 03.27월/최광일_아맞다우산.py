'''
백준 아맞다우산

문제
https://www.acmicpc.net/problem/17244

1) 예제 입력 통과 
2) 백준 제출시 15% 정도 통과후 실패 ㅠㅠ

--> 실패나는 엣지 케이스를 어떻게 찾을 것인가?
--> 코드상 로직은 어떻게 검증할 것인가? 

입력
7 6
#######
#SX..X#
#..####
#..X..#
#...X.#
#####E#

출력
14

입력
7 6
#######
#S....#
#..####
#.....#
#.....#
#####E#

출력
8

'''
from collections import deque
from itertools import permutations
import sys
from copy import *
read = sys.stdin.readline
global R,C,v,m,s,e,p,tm

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def clearV():
    global R, C, v, m, s, e, p, tm
    # print('*** Clear visited ***')
    v = [[-1 for c in range(C)] for r in range(R)]

def printV():
    global R, C, v, m, s, e, p, tm
    # print('*** Visited ***')
    for i in v:
        print(*i)

def printM(a):
    # global R, C, v, m, s, e, p, tm
    # print('*** Map ***')
    for i in a:
        print(*i)

def bfs(A,B): # 두 지점간의 최단 거리 구하기
    global R, C, v, m, s, e, p, tm
    y1,x1,y2,x2 = A[0],A[1],B[0],B[1]
    # print(f'y1,x1,y2,x2 = {y1,x1,y2,x2}')

    cnt = 0
    Q = deque()
    Q.append((y1,x1,cnt)) # 시작 포인터

    while Q:
        r,c,cnt  = Q.popleft()
        v[r][c] = cnt
        if r == y2 and c == x2:
            # print(' Found End !!! ')
            return cnt

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if v[nr][nc] != -1:
                continue
            if tm[nr][nc] == '#':
                continue
            Q.append((nr,nc,cnt+1))


def main():
    global R, C, v, m, s, e, p, tm

    C,R = map(int,read().rstrip().split())

    # create map
    m = [] # map
    s = [] # start
    e = [] # end
    p = [] # point lists
    for i in range(R):
        text = read().rstrip()
        temp = []
        for j in range(C):
            c = text[j]
            if c == 'S':
                s = [i,j]
            if c == 'E':
                e = [i,j]
            if c == 'X':
                p.append([i,j])

            if c == '#':
                temp.append('#')
            else:
                temp.append('.')
        m.append(temp)

    # 디버깅 코드 ---------------
    # clearV()
    # tm = deepcopy(m)
    # print(f'Start = {s}, End = {e}, Points = {p}')
    # printM(m) # 디버깅코드
    # tm[s[0]][s[1]] = 'S'
    # tm[e[0]][e[1]] = 'E'
    # for i in p:
    #     tm[i[0]][i[1]] = 'X'
    # printM(tm)
    # printV()
    # res = bfs(s,p[1])
    # 디버깅 코드 ---------------

    clearV()
    tm = deepcopy(m)

    permu = permutations(p)
    pathList = []
    for path in permu:
        temp = []
        temp.append(s) # Start 점 추가
        for j in path: # 거쳐야 하는 path 추가
            temp.append(j)
        temp.append(e) # End 점 추가
        pathList.append(temp) # S -> P1 -> P2 ... Px -> E

    # for i in pathList:
    #     print(*i)

    best = 10**6
    sum = 0
    for path in pathList:
        for i in range(len(path)-1):
            clearV()
            A = path[i]
            B = path[i+1]
            sum += bfs(A,B)
        best = min(best,sum)
    print(best)
    pass

if __name__ == '__main__':
    main()
