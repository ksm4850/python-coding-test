
n,m = map(int,input().split())
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()


from itertools import product
# 중복 순열을 구할 itertator와 조합의 개수(repeat)를 parameter로 받음
print(product([1,2,3], repeat = 2))