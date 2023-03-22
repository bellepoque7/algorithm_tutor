'''
전체 케이스중
 런타임 에러 8개
 시간초과 2 개
'''

def solution2(N, stages):
    # stages.sort()  # 굳이 sort로 시작할 필요가 있을까요?
    temp = 0
    result = [[] for i in range(N)]
    answer = []
    total = 0
    # 이미 O(n^2) TLE 유력 500 * 200,000 = 1억!
    for i in range(1,N+1) :  #stage 올라가며 체크 1번,2번,3번,,, N번
        for j in range(len(stages)) : #stages 리스트 순회하면서 하나씩 체크하기.
            if stages[j] < i :
                continue
            
            elif stages[j] == i :
                temp += 1 # 현재 확인하는 스테이지 값보다 같다면 트라이하고 있으므로 temp += 1
                total += 1 # 전체인원 추가
            elif stages[j] > i :
                total += 1 

        result[i-1].append(i)
        result[i-1].append(temp / total)
        total = 0
        temp = 0
    print(result)

    result = sorted(result, key = lambda x : (-x[1],x[0]))
    
    for i in range(N) :
        answer.append(result[i][0])
    print(answer)
    return answer


# solution2(5,[2, 1, 2, 6, 2, 4, 3, 3]) #[3,4,2,1,5]
# solution2(4,[4,4,4,4,4]) #[4,1,2,3]

#테스트
solution2(3,[1,1,1,1,1]) #[4,1,2,3] 오늘의 교훈: 나눌때는 분모가 0이되는 경우는 없는지 체크해라
