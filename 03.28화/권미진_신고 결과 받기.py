def solution(id_list, report, k):
    
    dic_id = {}
    dic_count = {}
    dic_mail = {}
    for i in id_list:
        dic_id[i] = []
        dic_count[i] = 0
        dic_mail[i] = 0
    # print(dic_id) 
    
    for i in report:
        key, value = i.split()
        if value not in dic_id[key]:
            dic_id[key] += [value]
            dic_count[value] += 1
           
    for i in id_list:
        if dic_count[i] >= k:
            for j in id_list:
                if i in dic_id[j]:
                    dic_mail[j] += 1
    res = []
    for i in id_list:
        res.append(dic_mail[i])
 
    return res
