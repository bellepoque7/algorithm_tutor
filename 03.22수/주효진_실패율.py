def solution(N, stages):
    fail =[] # 실패율 list
    a = len(stages)
    
    for i in range(1,N+1):
        if a !=0:
            fail.append((stages.count(i)/a,i))  # index와 함께 담아줌
            a -= stages.count(i)  # 모수 제거
        else:
            fail.append((0,i))  # 스테이지에 도달한 유저가 없는 경우
            continue
            
    fail=sorted(fail, key = lambda x:(-x[0],x[1]))

    answer = []
    for i in fail:
        answer.append(i[1])
    return answer
