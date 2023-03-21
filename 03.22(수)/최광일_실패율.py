def solution(N, stages):
    global v
    
    my_dic = {}
    acc_p = 0 # 누적 플레이어수 
    cur_p = 0 # 현재 플레이서수 
    num_p = len(stages) # 총 플레이어수 
    # v = [ [0,0] for _ in range(N+2)] # 0 ~ N+1 스테이지, 0은 사용하지 않음, N+1은 마지막 N 스테이지까지 클리어 한경우
    v = [[0,0] for _ in range(N+2)]

    for stg in range(1,N+2):

        cur_p =stages.count(stg)
        
        clear_p = num_p - acc_p
        fail_p = cur_p
        
        if clear_p != 0:
            failRate = fail_p / clear_p
        else:
            failRate = 0.0
        
        v[stg] = [failRate,stg]
        acc_p += cur_p
        
        print(f'stage({stg}) - ({fail_p}/{clear_p}) failRate = {v[stg]}, acc_p={acc_p},num_p={num_p}')

    v.pop(0) # 0번 스테이지 삭제
    v.pop() # N+1번 스테이지 삭제

    v_sorted = sorted(v, key=lambda x: (-x[0],x[1])) # failRate 내림차순 정렬하고 값이 같으면 stage 올림차순 정렬

    # print(v_sorted)
    answer = []
    for i in v_sorted:
        answer.append(i[1])
        
    print(answer)
    return answer

def main():
    global v
    
    test = []
    test.append([4,[2,2,2,2,2]])
    test.append([5,[2, 1, 2, 6, 2, 4, 3, 3]])
    test.append([4,[4,4,4,4,4]])
    test.append([4,[1,0,3,0,5]])
    
    res = []
    for N,stages in test:
        res = solution(N, stages)
        print(res)
        
    
if __name__ == '__main__':
    main()
