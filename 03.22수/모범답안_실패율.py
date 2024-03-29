'''
스스로 풀기전에 답안을 보지 마세용 !!!
'''

def solution(N, stages):
    answer = []
    length = len(stages)
    #스테이지 번호를 1부터 N까지 증가시킴
    for i in range(1,N+1):
        #해당 스테이지에 머물러 있는 사람의 수 계산
        cnt = stages.count(i)   # list.count() 메소드는 O(n)입니다.
        
        #실패율 계산
        if length ==0:
            fail = 0
        else:
            fail = cnt / length
        
        #리스트에 (스테이지 번호, 실패율) 삽입
        answer.append(i,fail)
        length -= cnt

    #실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key = lambda t: t[1], reverse=True)

    #정렬된 스테이지 번호 출력
    res = [i[0] for i in answer]
    return res
