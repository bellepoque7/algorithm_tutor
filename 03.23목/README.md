## 문제 풀기전에 하기 예시를 보지마세용 ~

### 1. 문제 예시

<img width="537" alt="image" src="https://user-images.githubusercontent.com/39439424/227134911-10b29e67-166d-46c9-a65d-eed77e4484ff.png">

<img width="521" alt="image" src="https://user-images.githubusercontent.com/39439424/227134949-00503f74-5089-4c82-af6f-09cb35148f6f.png">



[역시 시각화가 짱입니다](https://docs.google.com/spreadsheets/d/1Jf18u-kJ9rUhMqmRO3rO9SO_fU0VvCwDNYiRSEb-evk/edit#gid=0)

![image](https://user-images.githubusercontent.com/39439424/226937819-209cd93b-ed7d-42ea-b214-8a0773a466f8.png)

### 2. idea.

- 열쇠는 회전과 이동이 가능하다 -> 열쇠 회전하는 함수(rotaate_90), 이동 방법 구현(for문)
- 열쇠는 자물쇠의 경계를 넘어가도 된다 -> 그럼 자물쇠를 확장시키는 기능 구현
- 열쇠와 자물쇠가 맞는 조건 -> 자물쇠와 열쇠를 요소끼리 더하여  중앙 자물쇠 영역이 모두 1이 되면 맞는것. (그말인 즉슨 1개라도 틀리면 False, 따라서 기저조건 True)
- N이 굉장히 관대함. 4(방향) * (20x2) * (20x2) * 20* 20 = 2,560,000  

### 3. 변수 선언

- roate_90 함수(Input: 열쇠, output: 90도 회전 시킨 열쇠)
  - result: 90도 회전 시킨 열쇠
  - ex. 2Darray 기준으로 회전시키기: result[j][n-j-1] = a[i][j]

만약 위 로직이 생각 나지 않았다면, 예시에 대한 90도 돌리는거 직접 예시는 것도 방법

<img width="371" alt="image" src="https://user-images.githubusercontent.com/39439424/227097746-a25900ba-1419-45ed-a993-6ffbdfc76205.png">


- check 함수(Input: 3배 확장 시킨 자물쇠, output: Boolean)
  - lock_length: 확장시킨 자물쇠 길이의 1/3
- solution 함수(Input: 열쇠와 자물쇠, output: Boolean)
  - n: 자물쇠의 길이
  - m: 열쇠의 길이
  - lock: 자물쇠 2d array list
  - lock_3x: 3배 확장시킨 2d array list ~~이거완전 패딩??~~
  - key: 열쇠 2d array list


### 4. 기타

- 종부님 코드 어떻게 개선할까요?

현재 같은 크기만 해결할 수 있는 상태. 어떻게 개선할 수 있을까요? 가능은 할까요?

