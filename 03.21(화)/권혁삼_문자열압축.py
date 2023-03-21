def cut(i,s):
    
    A = []
    a = 'a'
    for j in s:
        a += j
        if len(a) == i+1:
            A.append(a)
            a = 'a'
    return A

def solution(s):
    
    result = len(s)
    s_length = len(s)//2
    # 1~길이/2까지 전부 확인!
    for i in range(1, s_length+1):
        #i개 기준으로 절단!
        B = cut(i,s)
        flag = True
        answer = len(s)
        cnt = 0
        # print(B)
        #다음항과 비교 
        for j in range(1,len(B)):
            # print(answer)
            if B[j-1] == B[j]:
                cnt += 1
                if cnt ==10:
                    answer +=1
                elif cnt == 100:
                    answer +=1
                elif cnt == 1000:
                    answer +=1
                if flag:
                    flag = False
                    answer += 1
                    answer -= i
                else:
                    answer -= i
            else:
                flag = True
                cnt=0
                    
        result = min(answer,result)        
                    
    return result
