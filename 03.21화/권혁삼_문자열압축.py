def cut(i,s):
    
    A = []
    a = 'a' #의미없는 문자열
    for j in s:
        a += j  # 문장열 합치기
        if len(a) == i+1:
            A.append(a)
            a = 'a'
    return A  # ['a a']

def solution(s):
    result = len(s)
    s_length = len(s)//2
    # 1~길이/2까지 전부 확인!
    for i in range(1, s_length+1):
        #i개 기준으로 절단!
        B = cut(i,s)
        flag = True  # 나중에 설명
        answer = len(s)  # int
        cnt = 0
        # print(B)
        #다음항과 비교 
        for j in range(1,len(B)):  #1부터 쪼갠 길이까지 루프
            # print(answer)
            if B[j-1] == B[j]:  #전문자열이 같으면 cnt +1
                cnt += 1
                if cnt ==10:     #
                    answer +=1
                elif cnt == 100:
                    answer +=1
                elif cnt == 1000:
                    answer +=1
                if flag:        # aa
                    flag = False
                    answer += 1 # 숫자가 들어가니까 1을 들어보낸다. 
                    answer -= i # 길이만큼 빼주기
                else:
                    answer -= i
            else:
                flag = True # 다른패턴 비교하기위해서 초기화
                cnt=0
        result = min(answer,result)        
    return result