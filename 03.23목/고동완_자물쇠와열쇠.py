##풀이 못함.못 풀어도 올려요..

##IDEA.. 
## 1) 먼저 key의 1의 숫자가 lock의 0의 숫자보다 크거나 같아야 열수 있는지 check
## 2) key의 행렬을 이중포문 돌면서 좌표로 받는다.
## 3) lock의 행렬을 돌면서 0을 만나면 1로 변경 후 방향 vector로 이동한다. 이 때 이동 횟수는 key의 1의 숫자에 해당하는 만큼만 이동할 수 있다.
       #key를 이동하고 회전하면 안 되는 경우는 일부 : ex)대각으로 key(1)가 위치해 있는데 행렬의 0(구멍)은 평행한 경우. >>방향vector로 대각선이 있나 없나..

def check(key,lock): #key의 1이 lock의 0의 개수보다 많아야 가능하다.
    count_key= 0
    count_lock=0
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == 1:
                count_key += 1

    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                count_lock += 1

    # print(count_key)  # 출력: 3
    # print(count_lock)
    if count_key>=count_lock:
        return True

    else :
        return False


# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

# 1이 존재하는 좌표를 찾아내는 함수
def find_ones(key):
    ones = []
    for i in range(len(key)):
        for j in range(len(key[i])):
            if key[i][j] == 1:
                ones.append((i, j))
    return ones

# 이동하는 방향을 나타내는 direction list를 만드는 함수
def make_dir(ones):
    dir = []
    for i in range(len(ones)-1):
        x_diff = ones[i+1][0] - ones[i][0]
        y_diff = ones[i+1][1] - ones[i][1]
        dir.append((x_diff, y_diff))
    return dir

def key_nums(key):  #key에서 몇 칸 이동할 수 있는지 확인
    cnt=0
    for i in key:
        for j in i:
            if j==1:
                cnt+=1
    return cnt

def solution(key, lock):
    print(check(key,lock))
    # # 실행 예시
    # ones = find_ones(key)
    # dir = make_dir(ones)
    # print(dir)  # 출력: [(1, 0), (-1, 1)]
    # print(key_nums(key))
    #
    # for j in range(key_nums(key)):
    #     nr = r + dir[j][0]
    #     nc = c + dir[j][1]
    #     if nr < 0 or nr >= R or nc < 0 or nc >= C:
    #         continue


def main():
    key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    solution(key, lock)

if __name__=='__main__':
    main()
