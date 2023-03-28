from itertools import combinations

def solution(relation):
    row = len(relation) # 행의 길이: 6
    col = len(relation[0]) # 열의 길이: 4

    #가능한 속성의 모든 인덱스 조합만들기
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    #print(combi)
    # [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

        
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        print(tmp) #[('100',), ('200',), ('300',), ('400',), ('500',), ('600',)]
        # break

        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
   
    return len(unique)

if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))