def solution(N, stages):
    from collections import deque

    # stages_sorted = sorted(stages)
    qu = deque(sorted(stages))

    fail_rate = [0] * (N+1)


    for i in range(1,N+1):
        # print(f' fail_rate:{fail_rate}')

        if len(qu) == 0:
            fail_rate[i] = 0.0

        elif len(qu):
            fail_rate[i] =  qu.count(i) / len(qu)
            # print(f'qu:{qu}')
            while 1:
                if not qu:
                    break
                if qu[0] == i:
                    qu.popleft()
                else:
                    break

    fail_rate_enumerate = []
    for num,rate in enumerate(fail_rate):
        if num == 0:
            continue
        fail_rate_enumerate.append((num,rate))

    fail_rate_enumerate = sorted(fail_rate_enumerate, key = lambda x: (-x[1],x[0]))

    answer = [x[0] for x in fail_rate_enumerate]


    return answer
