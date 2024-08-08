"""

두 분수 더하기

기약분수로 만들고 출력
"""

def gcd(x,y): #최대공약수, 유클리드 호제법
    while y:
        x,y = y,x%y
    return x    

A, B = map(int, input().split())
C, D = map(int, input().split())
N = gcd(A*D + C*B, B*D)
print((A*D + C*B)//N, B*D//N)