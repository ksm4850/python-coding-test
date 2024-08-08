"""
8*8

B 갯수 W 갯수 세고

B 32개 W 32개

"""

N,M = map(int,input().split())
original = []
count = []
for _ in range(N):
    original.append(input())

for a in range(N-7):  # 8*8로 자르기 위해 -7
    for b in range(M-7):
        W = 0 # 흰색으로 시작
        B = 0 # 검은색으로 시작
        for i in range(a, a+8): # 시작지점
            for j in range(b, b+8): # 시작지점
                if (i+j) % 2 == 0:  # i+j 가 짝수면
                    if original[i][j] != 'W': # W가 아니면
                        W += 1 # W로 칠할 갯수
                    if original[i][j] != 'B': # B가 아니면
                        B += 1 # B로 칠할 갯수
                else: # 홀수면
                    if original[i][j] != 'B':
                        W += 1
                    if original[i][j] != 'W':
                        B += 1
        count.append(min(W, B))
        
print(min(count))