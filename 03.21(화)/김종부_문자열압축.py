def solution(s):
    answer = [] #리턴값 받을 원소 저장
    if len(s) == 1: # 문자 길이 1일때는 1값 바로 리턴
        return 1
    
    for i in range(1,(len(s)//2)+1): # 최대 절반 자를 수 있음
        check = s[:i] # s문자열에서 초기 i개씩 잘라서 확인 (전부 탐색)
        b = '' # 문자열 더해서 받을 부분 생성
        cnt = 1 # 처음에 1개부터 시작
        for j in range(i,len(s),i): #j는 i부터 +i 인덱스까지 s끝까지 확인
            if check == s[j:j+i]: #초기 i부터 끝까지 문자열이랑 같은 배열이 있을 때는 cnt + 1
                cnt+=1
            else : #초기 i부터 끝까지 같은 배열 없을 때
                if cnt == 1: #cnt 1일때는 check한 문자만 더해줌 (절반)
                    b += check
                else : #cnt 1이외에는 갯수 표시 해야함  (한개이상 존재) ★이거 찾기
                    b += str(cnt) + check #반복 문자 앞에 갯수 더하기
             '''       
              #조건 더 생각 test 2개맞음
             '''       
        if cnt == 1:
            b += check
        else :
            b += str(cnt) +check
        answer.append(len(b)) # 더해진 b값 리스트에 넣기
    answer = min(answer) #리스트에서 최소값 찾기
    return answer
