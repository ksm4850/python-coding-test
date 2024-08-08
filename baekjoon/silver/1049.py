"""
N : 끊어진 기타줄
M : 기타줄 브랜드

각 브랜드 6개 , 1개 파는 가격
"""
N,M = map(int,input().split())

bundle = []
item = []


for _ in range(M):
    a, b = map(int,input().split())

    bundle.append(a)
    item.append(b)
# 묶음과 낱개의 최소값
bundle = min(bundle)
item = min(item)

if bundle < item * 6:
    if bundle < (N % 6) * item:
        print((N // 6) * bundle + bundle)
    else:
        print((N // 6) * bundle + (N % 6) * item)

elif bundle >= item * 6:
    print(N * item)
