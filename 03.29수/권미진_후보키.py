#정답

from itertools import combinations

def solution(relation):
    
    a = len(relation[0])
    res = []
    li = combi(a) #칼럼번호들의 조합  

    for comb in li:
        flag = True  #최소성 검증
        for i in res:
            if len(comb) == 1:   #1개 짜리 key는 최소성 검증 불필요
                continue
            # print(i, list(combinations(comb,len(i))))
            if i in list(combinations(comb,len(i))):
                flag = False
        
        if flag and check(comb,relation):
                res.append(comb)
    print(res)
    answer = len(res)
    return answer
  

# 조합만들기
def combi(a):
    comb = []
    for i in range(1,a+1):    #처음 오답 포인트 : range(a)로 하면 0개를 고르는게 생김, 최소 1개를 골라야함.
        comb += list(combinations(range(a),i))
    return comb    

#유일성 검증
def check(comb,relation):
    li = []  
    for i in relation:
        temp = []
        for j in comb:
            temp.append(i[j])
        li.append(temp)
    li_s = []
    for i in li :
        if i not in li_s:
            li_s.append(i)
    
    return len(li_s) == len(li)


#내장함수 사용하기
----------------------------------------------------------------------------------------------------
from itertools import combinations

def solution(relation):
    
    a = len(relation[0])
    
    
    # if a == 1:
    #     return 1
    
    res = []
    li = combi(a) #칼럼번호들의 조합
    
    
    for comb in li:
        flag = True  #최소성 검증
        for i in res:
            if len(comb) == 1:
                continue
            if set(i).issubset(set(comb)): #부분집함임을 확인하기
                flag = False
        
        if flag and check(comb,relation):
                res.append(comb)
    print(res)
    answer = len(res)
    return answer


def combi(a):
    comb = []
    for i in range(1,a+1):
        comb += list(combinations(range(a),i))
    return comb    

#유일성 검증
def check(comb,relation):  #리스트를 tuple로 변환하여 요소로 넣으면 set 함수 사용가능
    li = []  
    for i in relation:
        temp = []
        for j in comb:
            temp.append(i[j])
        li.append(tuple(temp))
    
    
    return len(set(li)) == len(li)

