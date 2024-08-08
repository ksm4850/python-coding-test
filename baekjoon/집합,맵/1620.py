import sys
input = sys.stdin.readline

N,M = map(int,input().split())

dic = {}
for i in range(1,N+1):
    name = str(input().strip())
    dic[name] = i
    dic[i] = name

for _ in range(M):
    a = str(input().strip())

    if a.isdigit():
        # 숫자면
        print(dic[int(a)])
    else:
        #문자면
        print(dic[a])
