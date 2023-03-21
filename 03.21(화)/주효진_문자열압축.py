###### 68점 코드##########

# 문자의 길이 check
def cal_lenth(arr):
    lenth = 0
    for i in arr:
        N, S = i
        if N != 1: # 반복된 문자
            lenth += (1 + len(S))
        else:
            lenth += len(S)
    return lenth

def solution(s):
    res =len(s)
    # 단어 2개씩, 3개씩 --- n개씩 문자 단위묶음 for문, s 길이 절반까지만 체크
    for i in range(2,len(s)//2+1):
        idx = 0
        li1 = []
        # 반복되는 문자 갯수 체크
        while idx+i < len(s):
            rep = s[idx:idx+i]  # 처음 문자 체크 후
            idx = idx +i
            cnt = 1 # 반복수
            while True:
                if s[idx:idx+i] != rep: # 처음 문자와 다르면 while문 break
                    break
                cnt +=1 # 처음 문자와 같으면 반복개수 +1
                idx = idx + i

            # (반복수, 반복문자) 저장
            li1.append((cnt,rep))
        li1.append((1,s[idx:]))

        res=min(res,cal_lenth(li1)) # 문자열 길이 작은값 갱신


    return res
