#100

def solution(id_list, report, k):
    N = len(id_list)
    id_dict = {}
    for idx,value in enumerate(id_list):
        id_dict[value]=idx
        
    V_list = [[] for _ in range(N)]
    V = [0 for _ in range(N)]
    answer = [0 for _ in range(N)]
    for condition in report:
        user,victim = condition.split(' ')
        for idx,value in enumerate(id_list):
            if victim == value:
                if user in V_list[idx]:
                    continue
                V_list[idx].append(user)
                V[idx] += 1
    
    # print(V_list)
    # print(V)
    answer_list=[]
    for i,v in enumerate(V_list):
        if V[i] >= k:
            for j in v:
                answer[id_dict[j]] += 1
            
        
    return answer
