# from collections import defaultdict

def solution(today, terms, privacies):
    
    today = int(''.join(list(today.split("."))))  #날짜를 숫자로 변환
    dic_term = {}
    for i in range(len(terms)):
        key, value = terms[i].split()
        dic_term[key] = int(value)
        
    answer = []
    cnt = 0
    for privarcy in privacies:
        date,type= privarcy.split()
        term = dic_term[type]
        cnt += 1                 #인덱스 대신 순서를 나타낼 변수
        #a = date_calc(date,term)
        #print(today,a)
        if today >= date_calc(date,term):     #(수집날짜 + 유효기간)인 날부터 폐기해야함.(전날까지 보관가능)  
            answer.append(cnt)
    return answer


def date_calc(date,term):
    Y,M,D = map(int, date.split('.'))
    D += term*28                              #기간을 일로 더해줌

    d_calc = divmod(D,28)                 #몫과 나머지를 튜플로 반환
    D = d_calc[1]
    M += d_calc[0]
        
    # 나누어 떨어지는 경우 날짜는 00일 일 수 없음
    if D == 0:
        M -= 1
        D = 28
        
    M_calc = divmod(M,12)
    M = M_calc[1]
    Y += M_calc[0]
    
    # 나누어 떨어지는 경우 00월 일 수 없음    
    if M == 0:
        Y -= 1
        M = 12
        
    # 1자리인 경우 앞에 0을 붙여 주기 위함
    M = "00"+ str(M)
    D = "00"+ str(D)
    result = str(Y) +M[-2:] + D[-2:] 
    
    return int(result)

    
    
