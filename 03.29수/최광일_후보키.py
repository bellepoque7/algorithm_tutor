'''
카카오 후보키

문제
https://school.programmers.co.kr/learn/courses/30/lessons/42890


--> primary key만 찾음
--> candidate key 중복 제거 실패 ㅠㅠ
--> 미구현 

입력
[["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]

출력
2


'''

def pr(relation):
    for i in relation:
        print(i)

def solution(relation):
    from itertools import combinations

    answer = 0

    pr(relation)
    C = len(relation[0])
    R = len(relation)

    pri_key = [1 for _ in range(C)]
    for c in range(C):
        temp = []
        for r in range(R):
            if relation[r][c] in temp:
               pri_key[c] = 0
            temp.append(relation[r][c])


    candi_key = []
    for i in range(C):
        if pri_key[i] == 0:
            candi_key.append(i)
        if pri_key[i] == 1:
            answer += 1


    print('pri_key = ',pri_key)
    print('candi_key = ', candi_key)

    candi_num = len(candi_key)

    foundKey = []
    for k in range(2,candi_num+1):
        comb = list(combinations(candi_key,k))
        print(comb)

        for i in comb:
            tempKey = []
            isFound = False
            for r in range(R):
                temp = []
                for j in i:
                    temp.append(relation[r][j])
                print(temp)
                if temp in tempKey:
                    isFound = True
                tempKey.append(temp)
                print(tempKey)
            if not isFound:
                # print()
                answer += 1
                foundKey.append(i)


        print('foundKey',foundKey)


    print('answer = ',answer)
    return answer

def main():

    tc = []
    tc.append([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
    for t in tc:
        solution(t)

if __name__ == '__main__':
    main()
