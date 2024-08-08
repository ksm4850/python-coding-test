n,m = map(int,input().split())
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)

from itertools import combinations_with_replacement
# 중복 조합을 구할 itertator와 조합의 개수를 parameter로 받음
print(list(combinations_with_replacement([1,2,3], 2)))