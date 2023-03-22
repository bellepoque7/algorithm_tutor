def solution(s):

    A = ""
    cnt = 1
    res = 1e9

    for i in range(1,len(s)+1):
        for j in range(0,len(s),i):
            if j+i <= len(s):
                if s[j:j+i] == s[j+i:j+2*i]:
                    cnt += 1
                else:
                    if cnt == 1:
                        A = A + (s[j:j+i])
                    else:
                        A = A + str(cnt) + s[j:j+i]
                        cnt = 1
            else:
                A = A + s[j:len(s)]
        res = min(res, len(A))
        A = ""
        
    return res
