def solution(id_list, report, k):

    report_dict = dict() ; final_report_dict = dict()

    for i in id_list:
        report_dict[i] = []
        final_report_dict[i] = []



    for i in report:

        a,b = i.split()
        if b not in report_dict[a]:
            report_dict[a].append(b)

    # print(f'report_dict:{report_dict}')

    reported_id=[]
    for a,b in report_dict.items():
        for j in b:
            reported_id.append(j)

    # print(f'reported_id:{reported_id}')

    reporting_num_dict=dict()

    for i in reported_id:
        if i in reporting_num_dict:
            reporting_num_dict[i]+=1
        else:
            reporting_num_dict[i] = 1

    stop_id_list=[]
    for name,reportnum in reporting_num_dict.items():
        if reportnum >= k:
            stop_id_list.append(name)

    # print(f'stop_id_list:{stop_id_list}')

    for name,report_name in report_dict.items():
        for j in report_name:
            if j in stop_id_list:
                final_report_dict[name].append(j)

    # print(final_report_dict)
    answer = []

    for a,b in final_report_dict.items():
        answer.append(len(b))

    # print(answer)





    # print(report_dict)
    # print(id_dict)


    return answer
