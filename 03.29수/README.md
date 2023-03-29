##


## 1. 문제 예시

<img width="500" alt="image" src="https://user-images.githubusercontent.com/39439424/228446899-16acc9b9-4263-4a4e-8a3c-f94bf89b210b.png">


## 2. 아이디어
- 문제 예시에서는 4가지의 컬럼이 있음. 따라서 4C1 + 4C2+ 4C3 + 4C4 의 조합 15가지가 나올 수 있음.
- 이 모든 것에 대해서 iteration 을 통하여 하기 2가지를 검정 하면 됨

<img width="1138" alt="image" src="https://user-images.githubusercontent.com/39439424/228446735-830dd555-2c17-4640-99c2-72fff63a8bff.png">

1. 유일성 체크
- 위 인덱스를 바탕으로 value를 입력하여 2d array 로 각각 만듬
<img width="1340" alt="image" src="https://user-images.githubusercontent.com/39439424/228426828-8b86aee4-05cc-4ce3-90b8-07af8174d8ee.png">
- set 함수를 통한 중복제거했을때, len(relation) 기본 입력 데이터의 행의 길이와 같다면 유일성 만족
- 또한 추후 최소성을 체크하기 위하여 Flag = True 선언

2. 최소성 체크
- 최소성은 유일성 이후 체크해야 하는 것이 포인트
- 최소성은 부분 집합의 개념을 이용. 

<img width="529" alt="image" src="https://user-images.githubusercontent.com/39439424/228427252-081ee043-6d10-41b4-8ecf-2df2787b741f.png">

- 위 그림에서 "학번(0번 인덱스)"와 "학번(0번 인덱스) + 이름(1번 인덱스)" 둘 다 유일성을 만족함
- but 전자가 후자의 부분 집합이기 때문에 굳이 이름까지 같이 쓰면서 후보키를 도출할 필요가 없음 
- 이를 코드단에서 구현하기 위하여 `set(x).issubset(set(col_idx))를 사용
- x가 col_idx의 부분 집합이면 True, 아니면 False 를 반환하는 함수
