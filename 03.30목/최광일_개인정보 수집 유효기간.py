'''

https://school.programmers.co.kr/learn/courses/30/lessons/150370

테스트 케이스 Fail 

datatime을 사용하는것아 아니라 year, month, day를 수동으로 28일로 계산해야하는가 ???

'''


from datetime import date

def solution(today, terms, privacies):
    answer = []
    print('today =', today)
    print('terms =', terms)
    print('privacies=', privacies)

    year, month, day = today.split('.')

    todayDate = date(int(year), int(month), int(day))
    print('*****')
    print('todayDate = ', todayDate)

    t_dic = {}
    for i in terms:
        t, m = i.split(' ')
        t_dic[t] = 28 * int(m)
        # t_dic.append((t,28 * int(m)))
    print(t_dic)

    p_list = []
    for i in privacies:
        d, t = i.split(' ')
        year, month, day = d.split('.')
        p_list.append((t, date(int(year), int(month), int(day))))
    print(p_list)

    cnt = 0

    over = []

    for p in p_list:
        p_date = p[1]
        delta = todayDate - p_date
        cnt +=1
        if delta.days >= t_dic[p[0]]:
            over.append(cnt)


        print(f'p_date = {p_date}, delta = {delta.days},terms = {p[0]},days = {t_dic[p[0]]}')

        # print('delta',t_date-todayDate)
    print(over)

    return answer

today = "2020.01.01"
terms = ['Z 3', 'D 5']
privacies= ['2019.01.01 D', '2019.11.15 Z', '2019.08.02 D', '2019.07.01 D', '2018.12.28 Z']

solution(today, terms, privacies)
