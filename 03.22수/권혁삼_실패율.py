def solution(N, stages):
    
    # stage 클리어 하지 못한 인원 수 check
    A = [0 for _ in range(N+2)]
    # stage 통과한 인원 check
    V = [0 for _ in range(N+2)]
    # print(A)
    for i in stages:
        A[i] += 1
        for j in range(i+1):
            V[j] += 1
            
    C = []
    result = []
    # stage별 실패율 계산
    for i in range(N+2):
        if V[i]==0:
            C.append(0)
            continue
        C.append(A[i]/V[i])
    # N+1 stage 제거
    C.pop()
    # stage 0 제거
    C.pop(0)
    
    #sort 위해 1-실패율로 변경
    for idx,value in enumerate(C):
        result.append((1-value,1+idx))
    answer = []
    
    result.sort()

    for i in range(len(result)):
        answer.append(result[i][1])
 
    return answer
