# 프로그래머스 모범답안

def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    # 각 약관에 대한 달을 dictionary 형태의 '약관종류':'달' 로 변경
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    # print(months) # {'A': 168, 'B': 336, 'C': 84},{'Z': 84, 'D': 140}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire

# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies  = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
solution(today, terms, privacies)