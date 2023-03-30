'''테케 3개 안맞음 85'''

def solution(today, terms, privacies):
    answer = []
    
    y,m,d = today.split('.') #현재 스트링 상태
    today = int(y+m+d)
    print(today)
    a = {} #알파벳_유효기간
    
    for i in terms:
        alphabet, month = i.split()
        a[alphabet] = int(month)
    print(a)

    for j in range(len(privacies)): 
        make_date,alpha = privacies[j].split() # 날짜, term
        year,month,day = map(int,make_date.split('.')) # 년,월,일
        month += a[alpha] 
        print(month)
        
        if month % 12 == 0:
            year += (month // 12) # -1 넣으면 테케 더맞음 ;
        else :
            year += month // 12 
            month = month % 12
            
        year,month,day = str(year),str(month),str(day)
        if len(month) == 1:
            month = '0' + month
        if len(day) == 1:
            day = '0' + day    
        if today >= int(year + month + day):
            answer.append(j+1)
    return answer
