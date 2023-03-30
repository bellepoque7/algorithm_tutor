

'테스트 케이스 19번만 실패 / 성공률 95% 코드'

def change_date(date) :

    temp_date = 0
    temp_date += int(date[2:4]) * 28 * 12
    temp_date += int(date[5:7]) * 28
    temp_date += int(date[8:10])
    return temp_date


def solution(today, terms, privacies):
    
    num_p = len(privacies)
    num_t = len(terms)
    answer = []
    today_date = change_date(today) +1
    date_p = []
    for i in range(num_p) :
        date_p.append(change_date(privacies[i]))
    print(today_date)
    print(date_p)
    
    for i in range(num_p) :
        for j in range(num_t) :
            if privacies[i][11] == terms[j][0] :
                if len(terms[j]) == 3 :
                    date_p[i] += int(terms[j][2])*28
                elif len(terms[j]) == 4:
                    date_p[i] += int(terms[j][2:4])*28
            else :
                continue

    
        if date_p[i] < today_date :
            answer.append(i+1)
    
    print(date_p)               
            

    return answer
