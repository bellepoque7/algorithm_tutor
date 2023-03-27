def solution(id_list, report, k):
    answer = []
    declaration = {}
    res = {}
    report = set(report)

    #초기화
    for i in id_list:
        declaration[i] = 0
        res[i] = 0
    
    #신고 당한 횟수 
    for i in report:
        id, declar = list(map(str, i.split()))
        declaration[declar] += 1
        
    #신고한 사람의 신고 횟수 조회 및 결과 저장
    for i in report:
        tmp_id, tmp_declar = list(map(str, i.split()))
        if declaration[tmp_declar] >= k:
            res[tmp_id] += 1 
    
    for key, value in res.items():
        answer.append(value)


    return answer


def main():
    # id_list = ["muzi", "frodo", "apeach", "neo"]
    # report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    # k = 2


    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3

    print(solution(id_list, report, k))


if __name__ == '__main__':
    main()
