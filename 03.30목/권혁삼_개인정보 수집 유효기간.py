#pass

def cal(yy,mm,dd):
    global ty,tm,td
    
    if mm>12:
        if mm%12!=0:
            yy += mm//12
            mm = mm%12
        else:
            yy += (mm-1)//12
            mm = (mm-1)%12+1
    # print(yy,mm,dd)
    if ty<yy:
        return False
    elif ty>yy:
        return True
    else:
        # print(1)
        if tm<mm:
            return False
        elif tm>mm:
            return True
        else:
            # print(1)
            if td<dd:
                return False
            elif td>=dd:
                return True
    # return True
    

def solution(today, terms, privacies):
    global ty,tm,td
    #terms 구분
    answer = []
    terms_dict = {}
    for term in terms:
        A,B = term.split()
        terms_dict[A] = int(B)
    # print(terms_dict) #확인
    
    #날짜 구분
    ty,tm,td = map(int,today.split('.'))
    # print(ty,tm,td) #확인
    
    #privacies 구분
    P = []
    for privacy in privacies:
        day,term = privacy.split()
        py,pm,pd = map(int,day.split('.'))
        pm += terms_dict[term]
        P.append((py,pm,pd))
    
    for idx,date in enumerate(P):
        py,pm,pd = date 
        if cal(py,pm,pd):
            answer.append(idx+1)
        
    # print(P)
    return answer
