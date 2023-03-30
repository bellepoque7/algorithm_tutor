
'질문하기 게시판에서 유효기간이 100달인 경우 엣지케이스 확인하고 처리해줌 / 성공률 100%'


def change_date(date) : # 문자열로 들어온 년/월/일을 다 일단위로 바꿈

    temp_date = 0
    temp_date += int(date[2:4]) * 28 * 12 #연도가 20XX년도이기 때문에 뒤에 XX년도만 숫자로 만듬
    temp_date += int(date[5:7]) * 28
    temp_date += int(date[8:10])
    return temp_date


def solution(today, terms, privacies):
    
    num_p = len(privacies)
    num_t = len(terms)
    answer = []
    today_date = change_date(today) +1 # 오늘 년/월/일을 일로 변환
    date_p = []
    for i in range(num_p) :
        date_p.append(change_date(privacies[i])) # 각 privacies에 들어온 년/월/일을 일로 변환
    print(today_date)
    print(date_p)
    
    for i in range(num_p) :
        for j in range(num_t) :
            if privacies[i][11] == terms[j][0] : # 개인정보와 유효기간의 알파벳이 같다면..
                if len(terms[j]) == 3 :
                    date_p[i] += int(terms[j][2])*28  # 유효기간 MM이 1의 자리일때
                elif len(terms[j]) == 4:
                    date_p[i] += int(terms[j][2:4])*28 # 유효기간 MM이 10의 자리일때
                elif len(terms[j]) == 5 :
                    date_p[i] += int(terms[j][2:5])* 28 # 유효기간 MM이 100의 자리일때


    
        if date_p[i] < today_date :
            answer.append(i+1)
    
    print(date_p)               
            

    return answer

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
