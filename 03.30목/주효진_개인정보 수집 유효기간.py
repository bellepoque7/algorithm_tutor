## pass

def solution(today, terms, privacies):
    prd = {}
    for i in terms:
        eng,month = i.split()
        prd[eng]=int(month)

    priv=[()]
    for i in privacies:
        dates,end = i.split()
        Y,M,D = map(int,dates.split('.'))
        priv.append((Y,M,D,prd[end]))
    deadline = []
    idx = 1
    M2 = 0
    for Y,M,D,t in priv[1:]:
        M2=M+t
        while M2>12:
            M2 -=12
            Y+=1
        D -=1
        if D ==0:
            D = 28
            M2 -=1
        deadline.append((idx,Y,M2,D))
        idx +=1

    YY,MM,DD = map(int,today.split('.'))
    answer = []
    for idx,Y,M,D in deadline:
        if Y>YY:
            continue
        elif Y==YY and M>MM:
            continue
        elif Y==YY and M==MM and D>=DD:
            continue
        answer.append(idx)

    return answer
