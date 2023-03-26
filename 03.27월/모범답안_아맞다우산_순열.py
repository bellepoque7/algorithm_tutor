from itertools import *
from collections import *

# 시작, 도착지점을 포함한 모든 지점이 depart, arrive 로 주어졌을때, bfs로 최단거리를 구함
def bfs(depart, arrive):
    global N,M, visited, visited_value, arr, stuff_cnt, graph
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()

    #bfs 수행시 출발,도착지점마다 따르게 메모리를 만들기 위해서 visited_value 설정
    visited[depart[0]][depart[1]] = visited_value
    q.append((*depart, 0))

    while q:
        x, y, k = q.popleft()
        for a in range(4):
            nx  = x+dx[a]
            ny  = y+dy[a]

            # bfs 중단조건 설정, 도착지점 만나면 k+1 리턴
            if (nx, ny) == arrive:
                return k+1

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] != visited_value and graph[nx][ny] != '#':
                visited[nx][ny] = visited_value
                q.append((nx, ny, k+1))
    return -1


# 한 지점에서 다른 지점을로 가는 모든 경우의 수에 대한 거리를 구함.
def get_distance():
    global N,M, visited, visited_value, arr, stuff_cnt, graph
    dist = [[0 for _ in range(stuff_cnt+2)] for _ in range(stuff_cnt+2)]
    visited_value = 0
    '''
    시작 array index -> 도착 array index
    0 1, 0 2, 0 3, 0 4, 0 5
    1 2, 1 3, 1 4, 1 5
    2 3, 2 4, 2 5
    3 4, 3 5
    4 5
    '''    
    for i in range(stuff_cnt+2): 
        for j in range(i+1, stuff_cnt+2):
            #bfs 수행시 출발,도착지점마다 따르게 메모리를 만들기 위해서 visited_value 설정
            visited_value += 1
            #출발과 도착지점의 최단거리를 dist 2d array에 저장
            d = bfs(arr[i], arr[j])
            dist[i][j] = d
            dist[j][i] = d
    # for i in range(M):
        # print(dist[i])
    '''
    예시: 0->1 인덱스는 1칸만에 도착, 0->2 인덱스는 4칸만에 도착. 대각행렬. 
    [0, 1, 4, 4, 6, 8]
    [1, 0, 3, 3, 5, 7]
    [4, 3, 0, 6, 8, 10]
    [4, 3, 6, 0, 2, 4]
    [6, 5, 8, 2, 0, 2]
    [8, 7, 10, 4, 2, 0]
    '''
    return dist

def solution():
    global N,M, visited, visited_value, arr, stuff_cnt, graph
    N, M = map(int, input().split())
    graph = []    # 그래프 저장
    depart = ()    # 시작좌표 저장
    end = ()      # 도착좌표 저장
    stuff = []    # 물건좌표 저장
    stuff_cnt = 0 #물건갯수 저장

    for i in range(M):
        r = input()   # 그래프 한줄씩 받아 처리하기
        graph.append(r)
        for j in range(N):
            if r[j] == 'S':  
                depart = (i, j)
            elif r[j] == 'E':  
                end = (i, j)
            elif r[j] == 'X':  
                stuff.append((i, j))
                stuff_cnt += 1

    arr = [depart, *stuff, end] # 시작,종료를 포함한 좌표 값 저장  ex. [(1, 1), (1, 2), (1, 5), (3, 3), (4, 4), (5, 5)]
    visited = [[0 for _ in range(N)] for _ in range(M)]
    # 한 지점에서 다른 지점을로 가는 모든 경우의 수에 대한 거리를 구함.
    my_dist = get_distance()
    min_td = 1e9
    
    '''1,2,3,4의 조합을 i 로 넣음
        (1,2,3,4),(1,2,4,3),(1,3,2,4) ...
    '''
    for i in permutations(range(1, stuff_cnt+1)):     
        '''
         앞뒤에 depart, end 순번 붙이기 [0, 1, 2, 3, 4, 5],[0, 1, 2, 4, 3, 5], [0, 1, 3, 2, 4, 5]
        '''
        route = [0]+list(i)+[stuff_cnt+1] 
        td = 0
        for i in range(stuff_cnt+1):
            td += my_dist[route[i]][route[i+1]]
        min_td = min(td, min_td)
    print(min_td)

solution()