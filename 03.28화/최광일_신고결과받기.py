'''

카카오 게시판 신고 받기

https://school.programmers.co.kr/learn/courses/30/lessons/92334

-> 100% 통과 ^^

입력
solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2])
출력
[2,1,1,0]

입력
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3])
출력
[0,0]

'''


def solution(id_list, report, k):
    # print(f'k={k},id_list = {id_list},report={report}')
    
    # Dictionary 생성 및 초기화 
    id_warning = {}
    id_email = {}
    for id in id_list:
        id_warning[id] = [] # 초기화
        id_email[id] = 0 # 0으로 초기화

    # 신고 처리 
    for r in report:
        A,B = r.split()
        if not A in id_warning[B]: # A가 들어 있지 않은 경우에만 추가
            id_warning[B].append(A) # B를 신고한 사람 추가
            # print(len(id_warning[B]))

    # 신고 결과 체크후 Email 발송
    for id in id_list:
        if len(id_warning[id]) >= k: # k번 이상 다른 사람에게 신고 된 경우
            for name in id_warning[id]:
                id_email[name] += 1 # Email 발송

    # print(id_warning)
    # print(id_email)

    answer = []
    for id in id_list:
        answer.append(id_email[id])

    # print(answer)

    return answer

def main():

    tc = []
    tc.append([["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2])
    tc.append([["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3])

    for t in tc:
        solution(t[0],t[1],t[2])
        print()

if __name__ == '__main__':
    main()
