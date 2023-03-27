# pass

def solution(id_list, report, k):
    answer = []
    result = {} 
    ban_id = {} # report 에서 신고당한 사람 넣기
    report = set(report) # report 안에 중복 되는 거 정렬해서 1개만 받음
    for i in id_list: #초기화
        result[i] = 0
        ban_id[i] = 0
    # print(report)
    
    for i in report: # report 안에서 신고한사람 신고당한 사람 나누기 [신고 당한사람 횟수 저장]
        a, b = i.split(" ")  
        ban_id[b] += 1 
    for i in report: 
        c, d = i.split(" ")
        if ban_id[d] >= k:
            result[c]+=1
            
    for key,value in result.items():
        answer.append(value)
    return answer
