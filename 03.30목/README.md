##


## 1. 문제 예시

## 2. 문제 풀이방법

- Q)날짜가 증가하는 것을 어떻게 처리할 것인가?
- 방법 1: 빡구현) 28일 넘어가면 +1달, 12달 넘어가면 +1년
- but, 2012-12-31 에서 1일 증가하면 년,월을 둘 다 바꿔야하는 귀찮음

- 방법 2: 모두 일수 로 변경) 모든 숫자를 월로 계산하여! 
- 자료구조를 통일하는것은 매우 중요합니다

### 자료구조 * 알고리즘 * 코드 길이 = 일정의 법칙

- 방법 3: datatime 함수이용 but customizing 귀찮음 pass
(https://docs.python.org/ko/3/library/datetime.html)

<img width="497" alt="image" src="https://user-images.githubusercontent.com/39439424/228772936-45e2ebec-8298-451f-92c8-8cc553a13251.png">


