"""
S = (A[0] * B[0]) + ... + (A[N-1] * B[N-1])

S의 값을 가장 작게 만드기 위해 A의 수를 재배열
B는 재배열하면안됨

S의 최솟값
"""

n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse=True)
B.sort()

result = [a * b for a, b in zip(A, B)]
print(sum(result))


# n = int(input())

# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# s = 0
# for i in range(n):
#     s += min(a_list) * max(b_list)
#     a_list.pop(a_list.index(min(a_list)))
#     b_list.pop(b_list.index(max(b_list)))

# print(s)