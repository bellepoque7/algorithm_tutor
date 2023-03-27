##


### 1. idea

- 물건 갯수가 관대함. 5개
- 시작, 끝지점을 포함하여 7개의 permuation을 돌려도 5040으로 크지 않음. 물건에 순서를 붙이고 모든 경우의대해서 정리해도 무리없음

### 2. 함수 설계

1. get_distance: 대각행렬로 출발도착 지점의 최단거리를 dist 2d array에 저장
- 출발,도착 지점별로 visited를 초기화 하는 것이 일반적
- vistied_count을 올려가며(1,2,3,4... )덮어 씌워서 체크해도 됨

2. bfs: 출발 도착 지점이 주어지면 bfs 수행
- input: 출발, 도착좌표, output: 이동거리 혹은 -1

3. solution: 메인함수

### 3. permutation 없이 구현할 수 없을까?
 
- visited 에 물건을 주운 기억(?)을 저장하면 됨.

<img width="769" alt="image" src="https://user-images.githubusercontent.com/39439424/227842320-3f30a653-fc81-45e7-82e1-4b292affab86.png">



- 물건 최대 5개이므로 00000으로 구현. 세번째를 주었다면 00100 첫번째의 물건도 주웠다면 10100 

  - ex. nbit = bit | (1 << pos)
    - `nbit`: 10100, `bit`:00100, `1<< pos` : 10000
    - |는 OR 연산자로 각 자리 수에 맞춰서 0,1 을 OR 연산
    - << 는 비트 연산자로 print(10<<1) 이면 10에 2^1을 한 20이 출력
  
- 5개라면 2^5 개이므로 visited[32][50][50] 로 3차원으로 구현
