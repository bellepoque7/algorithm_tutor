##
파일은 `임정_기둥과보` 와 같이 저장해주세요.

## 오늘의 추가 논의 

- 05:00 ~ 05:30:  기존 peer 피드백과 함께, 오답노트_실패율.py 의  개선이 필요한 점을 서로 논의해보세요
- ex) 런타임 에러난이유, TLE 난 이유, 반례


###  1. 예시 

### 2. 변수 선언

- cnt: stage 에 머물러 있는 사람수 계산

- fail: 실패율 계산

- answer: stage 별 실패율 저장(list)

- res: 결과


### idea

- n= 200,000 이므로 O(n^2)은 TLE(1억 이상) 따라서 O(nlogn)의 방법을 고민. 실제로 O(nlogn)은 3,400,000
- but! n= 500, m = 200,000  이면 O(NM)은 1억. 가까스로 가능할지도? [what is the time complexity of count](https://stackoverflow.com/questions/44812468/what-is-the-time-complexity-of-python-lists-count-function)

[Python 자료형별 time complexity](https://wiki.python.org/moin/TimeComplexity)

<img width="400" alt="image" src="https://user-images.githubusercontent.com/39439424/226795138-581184fa-477a-4f57-ba40-e38b6caa316b.png">

<img width="400" alt="image" src="https://user-images.githubusercontent.com/39439424/226795195-501c25c4-ac06-4e0b-a8f8-2562f6c7f125.png">

- 특이점: 
  - x in list은 O(n)  list의 길이가 길어지면 비효율적
  - x in dict은 O(1)  dict의 길이와 무관하게 상수시간 소요
- why?



<img width="600" alt="image" src="https://user-images.githubusercontent.com/39439424/226796724-3927f4dc-2d26-4fb8-9861-efb7cad86189.png">



## 오늘의 팁

### 1. enumerate
- 반복문을 돌릴때 range(len(my_list)) 대신 enumerate을 써보세요
- 성능이차는 아주 미묘하지만 가독성은 굉장히 좋아집니다. [rangelenlist-or-enumeratelist](https://stackoverflow.com/questions/11990105/rangelenlist-or-enumeratelist)

```
for i in range(len(my_list)):
  print(i, my_list[i])
  
for i,j in enumerate(my_list):
  print(i,j))
```
### 2. runtime error - divionbyzero
- 무엇인가 나눌때는 division by zero, 즉, 분모에 0에 가는 경우의 수는 없는지 체크해보세요


### 3.time complexity - buili-in func vs my code(T.T)
- python 으로 구현하기보다  내장함수를 써보세요 

ex. 1로 이루어진 1,000,000 개의 list의 합을 구해보자. 둘다 이론적으로는 시간복잡도 O(n)
- 방법1) my_list.count(1)
- 방법2) for 문을 이용한 더하기 

<img width="967" alt="image" src="https://user-images.githubusercontent.com/39439424/226835124-43d6d227-5966-4db3-983d-ce4edbe3a5e7.png">


### 3-1. 3/21 일일테스트 질문
문제: 풍선터트리기 

정답코드
deque[(1,1),(2,1),(3,1)]
```
deque.rotate(-2)
```
deque[(3,1),(2,1),(1,1)]


교육생 rotate 구현
```
for i in range(n):
  A,B = Deque.popleft()
  list.append((A,B))

```
- 결과 test case(n= 1000)일때 TLE
- 교훈: 파이썬 내장함수는 똑똑하다. 구현된 함수가 있으면 잘 써보자. 자주 쓰는 메소드의 time compexity를 잘 알면 좋다.
