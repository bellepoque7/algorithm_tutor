##


## 1. 문제 예시

<img width="500" alt="image" src="https://user-images.githubusercontent.com/39439424/228446899-16acc9b9-4263-4a4e-8a3c-f94bf89b210b.png">


## 2. 아이디어
- 문제 예시에서는 4가지의 컬럼이 있음. 따라서 4C1 + 4C2+ 4C3 + 4C4 의 조합 15가지가 나올 수 있음.
- 이 모든 것에 대해서 iteration 을 통하여 하기 2가지를 검정 하면 됨


1. 자료구조 선언
- 위 인덱스를 바탕으로 value를 입력하여 2d array 로 각각 만듬, for 문을 통한 증가하는 combination

```
for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
```
<img width="1138" alt="image" src="https://user-images.githubusercontent.com/39439424/228446735-830dd555-2c17-4640-99c2-72fff63a8bff.png">

- get_temp 함수: 위 인덱스를 가지고 모든 경우에 대한 Table을 만든다. 

<img width="61" alt="image" src="https://user-images.githubusercontent.com/39439424/228448502-624c9c01-9e4d-4615-9c2a-0c0767ca01d9.png">
- 유일성을 만족하지 않는 테이블 형태
<img width="102" alt="image" src="https://user-images.githubusercontent.com/39439424/228449154-fcb5c4a9-39e1-4bca-a921-790ca4446a54.png">
<img width="143" alt="image" src="https://user-images.githubusercontent.com/39439424/228448586-af54a270-f0a7-48d9-9f1a-1f83b6162795.png">
<img width="251" alt="image" src="https://user-images.githubusercontent.com/39439424/228448637-b648ba44-3913-403e-ad6d-73396ae24780.png">



2. 유일성 체크
- set 함수를 통한 중복제거했을때, len(relation) 기본 입력 데이터의 행의 길이와 같다면 유일성 만족
- 또한 추후 최소성을 체크하기 위하여 Flag = True 선언


3. 최소성 체크
- 최소성은 유일성 이후 체크해야 하는 것이 포인트
- 최소성은 부분 집합의 개념을 이용. 

<img width="529" alt="image" src="https://user-images.githubusercontent.com/39439424/228427252-081ee043-6d10-41b4-8ecf-2df2787b741f.png">

- 위 그림에서 "학번(0번 인덱스)"와 "학번(0번 인덱스) + 이름(1번 인덱스)" 둘 다 유일성을 만족함
- but 전자가 후자의 부분 집합이기 때문에 굳이 이름까지 같이 쓰면서 후보키를 도출할 필요가 없음 
- 이를 코드단에서 구현하기 위하여 `set(x).issubset(set(col_idx))를 사용
- x가 col_idx의 부분 집합이면 True, 아니면 False 를 반환하는 함수
