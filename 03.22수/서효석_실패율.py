def solution(N, stages):
    cnt=0
    res=[]
    Q=[0 for _ in range(N+2)]
    for stage_No in range(1,N+2):
        for i in stages:
            if i==stage_No:
                cnt+=1
        Q[stage_No]+=cnt
        cnt=0
    
    for i in range(1,N+2):
        x=Q[i]/sum(Q[i:])
        res.append((i,x))
    res=sorted(res,key=lambda x:(-x[1],x[0]))
    answer = []
    for i in res:
           answer.append(i[0])
    
    return answer
