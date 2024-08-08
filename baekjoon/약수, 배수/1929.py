N,M = map(int,input().split())

def check(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True # 소수

for i in range(N,M+1):
    if i == 1:
        continue
    if check(i):
        print(i)
