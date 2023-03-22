'''
문제 풀지 말고 열어보지마세요 ㅠ_ㅠ  로직을 스스로 고민해야 실력이 늡니다 !!
'''
def solution(s):
    answer = len(s)
    # 차근차근 1자리부터 전체문자열의 절반길이까지 loop 진행
    for step in range(1, len(s) // 2 + 1):
        # 압축 단위 설정
        prev = s[0:step]## s[0:1], s[0:2], s[0:3]...
        # 압축된 값 저장
        compressed = ''
        count = 1
        # prev 변수 가져와서 차근차근 비교하기, range 에 step 설정하여 건너뛰기
        for j in range(step, len(s), step):
            print(j,j+step)
            # prev 변수와 같으면 갯수 +1
            if prev == s[j:j+step]:
                count += 1
            # 만약 같지 않으면 패스 
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                '''
                compressed += str(count) + prev if count >= 2 else prev
                '''
                prev = s[j:j+step]
                count = 1
        if count >= 2:
                    compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer