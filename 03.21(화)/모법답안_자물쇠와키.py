'''
문제 풀지 말고 열어보지마세요 ㅠ_ㅠ  로직을 스스로 고민해야 실력이 늡니다 !!
'''

def solution(s):
  answer = len(s)
  # 1 step forward.
  for step in range(1,len(s) // 2 + 1):
    compressed = ''
    prev = s[0:step] # s[0:1], s[0:2], s[0:3]...
    count = 1
    # compare
    for j in range(step,len(s), step):
      # if same with previous one, plus count
      #slicing stirng.
      if prev == s[j:j + step]:
        count += 1
      # if another string appear(no more compressing)
      else:
        '''compressed += str(count) + prev if count >= 2 else prev'''
        if count >=2:
          compressed += str(count) + prev
        else:
          compressed += prev
        prev = s[j:j + step] # reset
        count =1
      # dealing with remains
      '''compressed += str(count) + prev if count >=2 else prev'''
      if count >=2:
          compressed += str(count) + prev
        else:
          compressed += prev
      # shortest is answer
      answer = min(answer, len(compressed))
    return answer
