'''

https://school.programmers.co.kr/learn/courses/30/lessons/150370

TC 100% 통과

1. 처음에 datetime 을 사용했는데 TC 통과 못함. 
2. 한달을 28일로 잡아야 한다는 조건때문에 날짜를 수동으로 계산하는 함수로 만들어서 패스함. 

'''


def calc(strDate):
    month2day = 28
    year,month,day = strDate.split('.')
    days = 0
    days += int(year) * 12 * month2day
    days += int(month) * month2day
    days += int(day)

    return days

def solution(today, terms, privacies):

    t_days = calc(today)

    answer = []
    # print(f'today = {today}, t_days = {t_days}')
    # print('terms =', terms)
    # print('privacies=', privacies)

    tDict = {}
    for i in terms:
        t,month = i.split(' ')
        tDict[t] = int(month)

    for i in range(len(privacies)):
        p_date,p_terms = privacies[i].split(' ')
        duration = tDict[p_terms] * 28
        
        # print(calc(p_date),t_days,duration)
        if t_days - calc(p_date)  >= duration:
            answer.append(i+1)
    # print(answer)
    return answer

today = "2020.01.01"
terms = ['Z 3', 'D 5']
privacies= ['2019.01.01 D', '2019.11.15 Z', '2019.08.02 D', '2019.07.01 D', '2018.12.28 Z']

solution(today, terms, privacies)
