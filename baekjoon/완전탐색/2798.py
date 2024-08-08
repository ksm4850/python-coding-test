"""
N : 카드 수 ( 3 <= N <= 100)
M : 숫자   ( 10 <= M <= 300,000)

M 과 최대한 가까운 카드 3장 고르기


"""
from itertools import combinations

card_num, target_num = map(int, input().split())

card_list = list(map(int,input().split()))

big_num = 0

for cards in combinations(card_list,3):
    temp_sum = sum(cards)

    if big_num < temp_sum <= target_num:
        big_num = temp_sum

print(big_num)


#-----------------------------------------------------------------
N,M = map(int, input().split())

arr = list(map(int,input().split()))

result = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)