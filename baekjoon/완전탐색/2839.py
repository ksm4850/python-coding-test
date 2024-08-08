"""
설탕봉지 3 , 8

최대한 적은 봉지 구하기

5의 배수가 될때까지 3씩 뺌
"""

n = int(input())

cnt = 0
while n >= 0:
    if n % 5 == 0 :  # 5의 배수이면
        cnt += (n // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(cnt)
        break
    n -= 3  
    cnt += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else:
    print(-1)