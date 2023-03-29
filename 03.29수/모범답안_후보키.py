from itertools import combinations
import pandas as pd


def get_tmp(col_idx,relation):
    '''
    col_idx(컬럼의 인덱스)를 전달받으면 해당 값을 가지고 2darray 를 만드는 함수 
    [('100',), ('200',), ('300',), ('400',), ('500',), ('600',)]
    .....
    [('100', 'ryan'), ('200', 'apeach'), ('300', 'tube'), ('400', 'con'), ('500', 'muzi'), ('600', 'apeach')]
    ....
    [('100', 'ryan', 'music', '2'), ('200', 'apeach', 'math', '2'), ('300', 'tube', 'computer', '3'), ('400', 'con', 'computer', '4'), ('500', 'muzi', 'music', '3'), ('600', 'apeach', 'music', '2')]
    '''

    tmp = []
    for item in relation:
        candidate = tuple([item[key] for key in col_idx])
        tmp.append(candidate)
    # print(tmp)
    # print(pd.DataFrame(tmp))
    return tmp


def solution(relation):
    row = len(relation) # 행의 길이: 6
    col = len(relation[0]) # 열의 길이: 4

    #가능한 속성의 모든 인덱스 조합만들기
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    # print(combi)
    # [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

        
    #유일성
    unique = []
    for col_idx in combi:

        #모든 컬럼의 조합을 만들어서 저장하기        
        tmp = get_tmp(col_idx,relation)
        # print(tmp)
    
        #1. 유일성 체크
        #모든 조합에 대해서 set 으로 중복제거
        #중복제거와 전체 길이가 같다면 유일성 만족
        if len(set(tmp)) == row:
            Flag = True
            
            # 첫번째 루프에서는 unique가 비어있어서 하기 for 문 수행되지 않음
            # 두번째 루프 unique = [(0)]
            for x in unique:

                #issubset메소드: x가 i의 부분 집합이면 True:
                #다시말해, unique 리스트에 있는 인덱스(컬럼의 번호)가 현재 i 의 부분집합이면 Flag = False
                # ex. 0,1컬럼으로 만든 후보키는 행을 식별할수있는 유일성을 가지지만, 
                # 이미 0 컬럼으로도 유일성을 가지며, 부분집합이기 때문에 최소성을 만족하지 않음
                if set(x).issubset(set(col_idx)):  # 최소성
                    Flag = False
                    break
            
            # 유일성과 최소성 체크된 컬럼이 인덱스만 unique 리스트에 넣기
            if Flag: 
                unique.append(col_idx)
                # print(unique) # [(0),(1,2)]
   
    return len(unique)

if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))