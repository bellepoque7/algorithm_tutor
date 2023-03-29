'''
50점..

후보키가 단일인것 까지만 구현되었고, 후보키가 2개 이상묶음일 때를 구현 못했습니다.
풀게 되면 업데이트 하겠습니당ㅠㅠㅠ
'''
from itertools import combinations

    # 중복 여부 체크
def set_f(arr):
    before = len(arr)
    res = set()
    for i in arr:
        res.add(i)
    after = len(res)
    return before == after

def solution(relation):
    col_len = len(relation[0])
    col = [[] for _ in range(col_len)]

    # col만 분류
    for row in relation:
        for idx, value in enumerate(row):
            col[idx].append(value)

    answer = 0
    # 후보키 갯수 찾기 (단일)
    for i in col:
        if set_f(i):
            answer += 1
            col.remove(i)
    #
    # comb = []
    # for i in range(1,len(col)+1):
    #     comb.append(combinations(range(col),i))
    # print(comb)

    # 후보키 갯수 찾기 (2개 이상)

    for i in range(2, len(col)+1):
        temp =[]
        for j in range(i-1):
            if len(temp)==0:
                a = col[j]
            else :
                a = temp
            b = col[j+1]
            temp = list(zip(a,b))
        if set_f(temp):
            answer +=1

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
