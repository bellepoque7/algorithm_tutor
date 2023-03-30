def solution(today, terms, privacies):
    # print(f'today:{today}')
    # print(f'terms:{terms}')
    print(f'privacies:{privacies}')

    term_dict=dict()
    for i in terms:
        term_type,month = i.split()
        term_dict[term_type] = int(month)
    today = tuple(map(int,today.split(".")))
    after_date=[]
    for i in privacies:
        date,term_type = i.split()
        year,month,day = map(int,date.split("."))
        add_month = term_dict[term_type]
        after_month = month + add_month
        # print(f'add_month:{add_month}')
        if after_month > 12:
            after_year = (after_month // 12) + year
            after_month = after_month % 12

        elif after_month <= 12:
            after_year = year

        after_date.append((after_year,after_month,day))
    # print(f'after_date:{after_date}')
    # print(f'today:{today}')

    answer = []

    for idx,date in enumerate(after_date):
        year,month,day = date
        if today[0] > year:
            answer.append(idx+1)
        elif year == today[0]:
            if today[1] > month:
                answer.append(idx+1)
            elif month == today[1]:
                if today[2] >= day:
                    answer.append(idx+1)



    return answer
