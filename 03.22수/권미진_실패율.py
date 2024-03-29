#1 
def solution(N, stages):

    temp = []
    players = len(stages)
    
    #인덱스 범위 설정
    #마지막 스테이지까지 도달한 사람이 없는 경우, 인덱스 에러 방지/*max(stages)+1로만 사용하면 안되는 이유 : N+1이 포함됨.(N+1 은 마지막 스테이지(N 번째 스테이지)까지 클리어 한 사용자)
    
    test_range = min(N+1, max(stages)+1)   

    for i in range(1,test_range):
        cur_p = stages.count(i)    #현 스테이지 클리어 못함사람
        f_rate = cur_p / players   #실패율
        temp.append((i, f_rate))  
        players -= cur_p           #다음스테이지에 도달한 사람들 계산

    temp = sorted(temp, key=lambda x: (x[1], -x[0]), reverse=True)
    answer = [x[0] for x in temp]
    if len(answer) < N:
        for i in range(test_range,N+1):
            answer.append(i)
    return answer

#2
def solution(N, stages):
    temp = []
    players = len(stages)

    for i in range(1, N + 1):
        if players == 0:
            temp.append((i, 0))
            continue
        cur_p = stages.count(i)
        f_rate = cur_p / players
        temp.append((i, f_rate))
        players -= cur_p

    temp = sorted(temp, key=lambda x: (x[1], -x[0]), reverse=True)
    answer = [x[0] for x in temp]

    return answer
