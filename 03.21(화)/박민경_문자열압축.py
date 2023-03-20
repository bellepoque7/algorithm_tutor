def solution(S):
    ans = []
    for unit in range(1, len(S)):
        tmp = []
        for i in range(0, len(S), unit):
            tmp.append(S[i:i+unit])
        tmp.append(' ')
        
        
        cnt = 0
        res = []
        for i in range(1, len(tmp)):
            if tmp[i-1] != tmp[i]:
                if cnt != 0:
                    res.append(str(cnt+1))
                res.append(tmp[i-1])
                cnt = 0
            else:
                cnt += 1

        ans.append(''.join(res))

    min_len = int(1e9)
    for i in ans:
        min_len = min(min_len, len(i))

    return min_len
