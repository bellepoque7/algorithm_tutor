## 1.문제 예시

## 2. idea

- solution 함수
- input: id_list, report, k, output:result

dictionary 를 써보자

- answer: 정답을 담을 list
- report: 중복신고 제거 set -> list
- user: 유저별 신고 id 저장 dict
- cnt: 유저별 신고당한 횟수 저장 dict



## 3. 번외) 예외처리하기 방법 3가지

1. if조건문 + dict

![image](https://user-images.githubusercontent.com/39439424/228000016-e25723d0-8130-4d70-a080-96ffdcf5fe11.png)


2. dict의 setdefault 메소드

![image](https://user-images.githubusercontent.com/39439424/228000077-5aeaeda8-6cfb-449e-9d95-0bcaa72bcbbc.png)


3. collections 모듈의 defaultdict

![image](https://user-images.githubusercontent.com/39439424/228000393-fb32c761-46d2-42a4-989c-5ff6449b10ce.png)


[딕셔너리 기본값처리](https://www.daleseo.com/python-collections-defaultdict/)
