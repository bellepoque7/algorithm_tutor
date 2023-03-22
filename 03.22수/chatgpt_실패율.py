#<런타임에러>


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

        # 예외 처리 추가
        if total == 0:
            result[i-1].append(i)
            result[i-1].append(0)
        else:
            result[i-1].append(i)
            result[i-1].append(temp / total)

        total = 0
        temp = 0
    result = sorted(result, key = lambda x : (-x[1],x[0]))
    
    for i in range(N) :
        answer.append(result[i][0])
    print(answer)
    return answer

# solution(5,[2, 1, 2, 6, 2, 4, 3, 3]) #[3,4,2,1,5]
# solution(4,[4,4,4,4,4]) #[3,4,2,1,5]

런타임 에러는 코드가 실행 중에 예상치 못한 오류가 발생하여 프로그램이 
비정상적으로 종료되는 경우를 말합니다. 따라서 런타임 에러가 발생하는 원인은 다양합니다.

해당 코드에서 런타임 에러가 발생할 가능성이 있는 부분은 for 루프에서 인덱스를 벗어나는 경우입니다. 
예를 들어 stages 리스트에 N보다 큰 숫자가 포함되어 있을 경우, N번째 스테이지를 처리하면서 stages 
리스트의 범위를 벗어나는 IndexError가 발생할 수 있습니다.

또한, 0으로 나누는 경우 ZeroDivisionError가 발생할 수 있습니다. 예를 들어, 해당 스테이지에 
도달한 플레이어가 없어서 total 변수의 값이 0이 되는 경우, temp 변수를 total로 나눌 때 ZeroDivisionError가 발생할 수 있습니다.

따라서 해당 코드에서는 이러한 예외 상황에 대한 처리가 필요합니다. 예를 들어, 
stages 리스트에 N보다 큰 숫자가 포함되어 있을 경우에는 해당 원소를 무시하거나, ZeroDivisionError가 발생할 가능성이 있는 경우에는 
조건문으로 분기를 나누어 예외 상황에 대응할 수 있습니다.
