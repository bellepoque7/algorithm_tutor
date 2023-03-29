# 못풀었음 포기


def solution(relation):
    from itertools import combinations

    zip_list = list(zip(*relation))
    length = len(zip_list[0])
    print(f'zip_list:{zip_list}')
    candidate_key=[]

    for num,i in enumerate(zip_list):
        temp_set=set()
        for j in i:
            temp_set.add(j)
        print(temp_set)
        if len(temp_set) == length:
            candidate_key.append(num)

    print(f'num:{candidate_key}')

    for num in candidate_key:
        del zip_list[num]

    return_list = list(zip(*zip_list))
    # zip_list_pair = list(combinations(zip_list,2))
    #
    # print(f'zip_list_pair:{zip_list_pair}')
    #
    # for i in zip_list_pair:

    print(f'return_list:{return_list}')

    print(f'zip_list:{zip_list}')




    return  candidate_key
