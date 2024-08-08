"""
permutation
"""
n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()


from itertools import permutations
# 순열을 구할 itertator와 조합의 개수를 parameter로 받음
print(permutations([1,2,3], 2))