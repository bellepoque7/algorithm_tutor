## 문제 풀기전에 하기 예시를 보지마세용 ~

### 1. 문제 예시


### 2. idea.

- 열쇠는 회전과 이동이 가능하다 -> 열쇠 회전하는 함수(rotaate_90), 이동 방법 구현(for문)
- 열쇠는 자물쇠의 경계를 넘어가도 된다 -> 그럼 자물쇠를 확장시키는 기능 구현
- 열쇠와 자물쇠가 맞는 조건 -> 자물쇠와 열쇠를 요소끼리 더하여  중앙 자물쇠 영역이 모두 1이 되면 맞는것. 
- N이 굉장히 관대함. 4(방향) * (20*2) * (20*2) * 20* 20 = 2,560,000  

### 3. 변수 선언

- roate_90 함수(Input: 열쇠, output: 90도 회전 시킨 열쇠)
  - result: 90도 회전 시킨 열쇠
- check 함수(Input: 3배 확장 시킨 자물쇠, output: Boolean)
  - lock_length: 확장시킨 자물쇠 길이의 1/3
- solution 함수(Input: 열쇠와 자물쇠, output: Boolean)
  - n: 자물쇠의 길이
  - m: 열쇠의 길이
  - lock: 자물쇠 2d array list
  - lock_3x: 3배 확장시킨 2d array list ~~이거완전 패딩??~~
  - key: 열쇠 2d array list


### 4. 기타


[역시 시각화가 짱입니다](https://docs.google.com/spreadsheets/d/1Jf18u-kJ9rUhMqmRO3rO9SO_fU0VvCwDNYiRSEb-evk/edit#gid=0)

![image](https://user-images.githubusercontent.com/39439424/226937819-209cd93b-ed7d-42ea-b214-8a0773a466f8.png)
