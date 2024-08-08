N = int(input())
for _ in range(N):
    A,B = map(int,input().split())

    a,b = A,B
    # 최대공약수
    while b!=0:
        a = a%b
        a,b = b,a

    print(A*B//a)