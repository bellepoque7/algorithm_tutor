'''
역량평가 때 순열로 경로를 만들고 bfs를 전체 경로로 돌려서 테케 2개 맞고 나머지 테케는 모두 시간초과되었습니다.
아래 풀이는 최성영님 풀이방법 참고해서, 먼저 graph 배열을 만들어서 bfs를 모든경로가 아닌 각 지점별 최소거리를 먼저 구성하고
순열에 따라 각 거리를 계산하였습니다~!
'''

from collections import deque
from itertools import *

dr = [-1,1,0,0]
dc = [0,0,-1,1]
global C,R,a
def bfs(sr,sc,er,ec):
    Q=deque()
    Q.append((sr,sc))
    visited=[[0 for i in range(C)] for j in range(R)]
    visited[sr][sc]=1

    while len(Q)>0:
        r,c = Q.popleft()
        if r == er and c == ec:
            return visited[r][c]-1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr<0 or nr>=R or nc<0 or nc>=C or a[nr][nc]=='#' or visited[nr][nc]!=0:
                continue
            Q.append((nr,nc))
            visited[nr][nc] = visited[r][c]+1

def main():
    global C,R,a
    C,R = map(int,input().split())
    a = []
    for _ in range(R):
        a.append(list(input()))

    path =[]

    for i in range(R):
        for j in range(C):
            if a[i][j]=='S':
                sr,sc = i,j
            elif a[i][j]=='X':
                path.append((i,j))
            elif a[i][j]=='E':
                er,ec = i,j

    path2 = [(sr,sc)] + path + [(er,ec)]
    graph = [[0 for i in range(len(path2))]for j in range(len(path2))]
    for i in range(len(path2)):
        for j in range(len(path2)):
            if i == j :
                graph[i][j] =0
            else:
                graph[i][j] = bfs(path2[i][0],path2[i][1],path2[j][0],path2[j][1])

    per = list(permutations(path,len(path)))

    res = 1e9
    for p in per:
        go = [(sr,sc)] + list(p) + [(er,ec)]
        temp = 0
        for i in range(len(go)-1):
            temp += graph[path2.index(go[i])][path2.index(go[i+1])]
        res = min(temp,res)

    print(res)

if __name__ == '__main__':
    main()
