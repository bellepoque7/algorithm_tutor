# pass

def check(today, date, period):
    tyear, tmonth, tday = map(int, today.split('.'))
    year, month, day = map(int, date.split('.'))

    ex_year = ex_month = ex_day = 0
    ex_month = month + period
    ex_year = year

    # 약관 입력이 100개월 까지 가능하므로 
    while ex_month > 12:
        ex_month -= 12
        ex_year += 1
    
    # 약관 날짜가 1일인 경우, 전 달 28일로 계산
    ex_day = day - 1
    if ex_day == 0:
        ex_month -= 1
        ex_day = 28

    # 만료인 경우 True
    if tyear > ex_year:
        return True
    elif tyear == ex_year and tmonth > ex_month:
        return True
    elif tyear == ex_year and tmonth == ex_month and tday > ex_day:
        return True

    return False



def solution(today, terms, privacies):
    answer = []

    dic = {}
    for i in terms:
        term, period = i.split()
        period = int(period)
        dic[term] = period
    
    for idx, case in enumerate(privacies):
        date, term = case.split()
        if check(today, date, dic[term]):
            answer.append(idx+1)
            
    return answer



# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# [1, 3]

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# [1, 4, 5]

print(solution(today, terms, privacies))
