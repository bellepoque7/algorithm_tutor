
n,m = map(int,input().split())
a = list(map(int,input().split()))

# print(n,m,a)

cnt = [0 for i in range(max(a))]
for i in range(max(a)+1):
    cnt[i-1] = a.count(i)

# print(cnt)

cnt_i = [[i,a] for i,a in enumerate(cnt,1)]
res = [ ]
for i in cnt_i:
    res.append([i[0],i[1]/sum(cnt[i[0]-1:])])

res2 = sorted(res,key = lambda x : x[1],reverse = True)
# print(res2)

for i in range(1,len(res2)): 
    # print(i)
    print(res2[i][0],end = ' ')
