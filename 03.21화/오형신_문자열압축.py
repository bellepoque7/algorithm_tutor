a = input()
res = []

for i in range(1,(len(a)+1)//2+1): # 끊는 단위 (반토막까지 예) 8개인경우 1 ~ 5 : 1,2,3,4) 
    a2 =  ''
    cnt = 1
    front = a[:i]

    for j in range(i,len(a)+i,i): # i 간격으로 비교작업 (예) 최대값 4개 vs 4개 , 12 (8+4 = 12 제외)) 
        print(j)
        if front == a[j:i+j]: # i 간격시 비교해서 같으면 cnt 추가 
            cnt += 1
        
        else:
            if cnt != 1:  # 해당 interval에 중복이 있으면  
                a2 = a2 + str(cnt)+ front # 숫자와 문자 조합으로 담음 
            else:
                a2 = a2 + front # 중복이 없으면 그냥 문자 그대로 추가 

            front = a[j : j+i] # 최초 0 ~2에서 비교 한 후 front를 2 ~4로 변경해줌 
            cnt = 1 # cnt는 1로 다시 reset 

    res.append(len(a2))
    
print(min(res))
