num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()
answer = 0
for i, num in enumerate(n[::-1]):
    # 36 ** 자리수 * 수
    answer += int(b) ** i * num_list.index(num)

print(answer)

# 아래방법도 가능
# n, b = map(str,input().split())
# print(int(n,int(b)))