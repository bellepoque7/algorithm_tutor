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
