def solution(N, stages):
    res = []
    cnt = len(stages)
    ans = []

    for i in range(1, N+1):
        if cnt == 0:
            res.append((i, 0))
            continue
        cur_stage = stages.count(i)
        res.append((i, cur_stage / cnt))

        cnt -= cur_stage

    res = sorted(res, key= lambda x : x[1], reverse=True)
    for i in res:
        ans.append(i[0])

    return ans
