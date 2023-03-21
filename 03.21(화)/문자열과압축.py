'모르겠습니다'

def solution(s):
    start = 0
    end = 1
    comp = []
    result = []
    cnt = 1

    for i in range(1, len(s)) :
        for j in range(0, len(s), cnt) :
            if s[j:i] == s[j:] :
                result.append(j-i)
                

    return answer
