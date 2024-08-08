import sys
sys.setrecursionlimit(int(1e6)) # 재귀함수 한계 풀어줌

n = int(input())
nums = [list(map(int,input().split()))for _ in range(n)]

def pooling(size,x,y):
    mid = size//2
    if size == 2:
        answer=[nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        answer.sort()
        return answer[-2]
    lt = pooling(mid,x,y) # 1사분면
    rt = pooling(mid,x+mid,y) # 2사분면
    lb = pooling(mid,x,y+mid) # 3사분면
    rb = pooling(mid,x+mid,y+mid) # 4사분면
    answer = [lt,rt,lb,rb]
    answer.sort()
    return answer[-2]

print(pooling(n,0,0))
