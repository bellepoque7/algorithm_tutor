
'정답률 100% 풀이'
def solution(N, stages):
    stages.sort()
    temp = 0
    result = [[] for i in range(N)]
    answer = []
    total = len(stages)
    for i in range(1,N+1) :
        temp = stages.count(i) #현재 가지고 있는 스테이지 인원 카운팅
        
        if total == 0 :
            result[i-1].append(i) #아무도 해당 스테이지 도달하지 못했을 때 실패율 계산
            result[i-1].append(0)
        else :
            result[i-1].append(i) # 스테이지 인덱스 값 저장
            result[i-1].append(temp / total) #스테이지 실패율 저장
            total -= temp #스테이지별 인원 감소시키기

        
        

    result = sorted(result, key = lambda x : (-x[1],x[0]))
    
    for i in range(N) :
        answer.append(result[i][0])
    

    return answer


'정답률 63% 풀이'

def solution(N, stages):
    stages.sort()
    temp = 0
    result = [[] for i in range(N)]
    answer = []
    total = 0
    for i in range(1,N+1) :
        for j in range(len(stages)) :
            if stages[j] < i :
                continue
            
            elif stages[j] == i :
                temp += 1
                total += 1
            elif stages[j] > i :
                total += 1
        result[i-1].append(i)
        result[i-1].append(temp / total)
        total = 0
        temp = 0

    result = sorted(result, key = lambda x : (-x[1],x[0]))
    
    for i in range(N) :
        answer.append(result[i][0])
    

    return answer
