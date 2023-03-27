## 결과 : pass
## panalty 배열을 만들어서 panalty[신고자][신고당한사람]으로 값을 표기
## out은 각 신고당한사람의 누적 panalty 표기
## 누적 패널티가 k보다 큰 사람을 신고했으면 cnt+1해서 answer 구성함.


def solution(id_list, report, k):
    n = len(id_list)
    panalty = [[0 for i in range(n)] for j in range(n)]
    out = [0 for _ in range(n)]

    def idx(name):
        return id_list.index(name)

    for i in report:
        a, b = i.split()
        if panalty[idx(a)][idx(b)] != 1:
            panalty[idx(a)][idx(b)] = 1
            out[idx(b)] +=1

    answer = []
    for i in range(n):
        cnt = 0
        for j in range(n):
            if panalty[i][j]>=1 and out[j]>=k:
                cnt +=1
        answer.append(cnt)

    return answer
