'''
## 풀이 못했지만 현재까지 작성 코드 올립니다.

방향 : 자물쇠 좌표에 회전을 포함한 열쇠좌표들이 방문, 열쇠의 튀어나온 부분을 dfs로 방문할때 자물쇠의 들어간 부분이 모두 방문 처리되면 true, 아니면 false
  1) 자물쇠의 좌/우 m-1씩 확장(visited)해서 만들어서 열쇠가 튀어나와도 되도록 고민
  2) 열쇠 이동을 못해서 현재 이 부분 구현 고민 중.
'''


global n,m,visited
dr = [-1,1,0,0,-1,-1,1,1]
dc = [0,0,-1,1,-1,1,-1,1]

def dfs(r,c):
    visited[r][c] =1

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        for j in range(m-1,2m):
            for k in range(m-1,2m):
        if key[nr][nc] !=1 and visited[nr+j][nc+k] ==1:
            continue
        dfs(nr,nc)

def solution(key, lock):
    global n,m,visited
    n = len(lock[0])
    m = len(key[0])
    visited = [[2 for i in range(n+2m-2)] for j in range(n+2m-2)]

    for i in range(n):
        for j in range(n):
            if lock[i][j]==1:
                visited[i+2][j+2] = 1
            elif lock[i][j]==0:
                visited[i+2][j+2] = 0

    answer = False

    for _ in range(4):
        for i in range(m):
            for j in range(m):
                dfs(i,j)
                if 0 not in visited:
                    answer = True
        if answer == False:
            key = list(map(list,zip(*key[::-1])))

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
