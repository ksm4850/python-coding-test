"""

"""

# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

import math
n,m = map(int,input().split())
print(math.factorial(n) // (math.factorial(m) * math.factorial(n-m)))
