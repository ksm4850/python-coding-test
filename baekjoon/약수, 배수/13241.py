"""
두 수의 최소공배수
"""

A,B = map(int,input().split())

a,b = A,B

# 최대공약수(유클리드 호제법)
while b!=0:
    a = a%b
    a,b = b,a

print(A*B//a)