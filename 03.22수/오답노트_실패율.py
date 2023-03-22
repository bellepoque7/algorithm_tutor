'''
전체 케이스중
 런타임 에러 8개
 시간초과 2 개
'''

def solution(N, stages):
    stages.sort()  # Q) 굳이 sorting 할필요가 있었을까요?
    temp = 0
    result = [[] for i in range(N)]
    print(result)
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
    print(answer)
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3]) #[3,4,2,1,5]
solution(4,[4,4,4,4,4]) #[3,4,2,1,5]