n = int(input())
p = [0] + list(map(int, input().split()))
# 문제와 인덱스 맞추기 위해 [0]에 0을 넣음
dp = [0 for _ in range(n+1)]
# p[i] = k개가 들어있는 카드팩 가격
# dp[i] = 카드 i개 구매하는 최대 가격

for i in range(1, n+1):
    for j in range(1,i+1):
        # 점화식 
        # 현재 카드를 지불하는 최대금액 ,이전 카드를 지불한(i-j) 최대금액 + j개가 들어있는 카드 가격 비교
        dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])