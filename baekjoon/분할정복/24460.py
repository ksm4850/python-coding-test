import sys
sys.setrecursionlimit(int(1e9)) # 재귀함수 한계 풀어줌

n = int(input())
nums = [list(map(int,input().split()))for _ in range(n)]

def sol(size,x,y):
    mid = size//2
    if size == 1:
        return nums[x][y]
    if size == 2:
        answer=[nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        answer.sort()
        return answer[1]
    lt = sol(mid,x,y) # 1사분면
    rt = sol(mid,x+mid,y) # 2사분면
    lb = sol(mid,x,y+mid) # 3사분면
    rb = sol(mid,x+mid,y+mid) # 4사분면
    answer = [lt,rt,lb,rb]
    answer.sort()
    return answer[1]

print(sol(n,0,0))