"""
combination
"""
n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)


from itertools import combinations
# 조합을 구할 itertator와 조합의 개수를 parameter로 받음
print(combinations([1,2,3], 2))