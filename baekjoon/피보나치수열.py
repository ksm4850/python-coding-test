#일반함수
# def fibo(n):
#     a,b = 0,1
#     for _ in range(n):
#         a,b = b,a+b
#     return a

# print([fibo(x) for x in range(1,10)])


# 제네레이터 구현
# def fibs(n):
#     a,b = 0,1
#     for _ in range(n + 1):
#         yield a
#         a,b = b, a+b

# fib = fibs(5)
# for i,val in enumerate(fib):
#     print(str(val),end=' ')


# #재귀함수
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# print(fib(10))


# DP 구현 (bottom_up)
# def fib(n):
#     fibList=[1, 1]
#     if n==1 or n==2:
#         return 1
#     for i in range(2,n):
#         fibList.append( fibList[i-1] + fibList[i-2] )
#     return fibList

# print(fib(3))

# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# n = 50
# print(fib(n))


# 람다를 사용한 한줄코딩
# fib = lambda n: 1 if n<=2 else fib(n-1) + fib(n-2)

# print(fib(5))
