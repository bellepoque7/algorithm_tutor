##
파일은 `임정_기둥과보` 와 같이 저장해주세요.


### 1. 예시 연습


- "aabbaccc"	 -> 7
- "ababcdcdababcdcd" ->	9
- "abcabcdede" ->	8
- "abcabcabcabcdededededede" ->	14
- "xababcdcdababcdcd" -> 	17



### 2. 변수 선언

- answer: 결과 담을 변수(string)

ex) s: aabbaccc   -> 2a2ba3c

- compressed: 압축할 단위 문자열(string)

- count: compressed 변수의 반복 횟수

- prev: count 변수와  compressed 변수의 합체

### 3. idea


- s 의 문자열은 1~1000 범위. 따라서 이중루프를 통한 완전 탐색 괜찮다!
- len(compressed)의 후보는 1부터 len(s)의 절반. 따라서 반복문 Range


