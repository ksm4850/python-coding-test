num1 = set(range(1,10001))
num2 = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num2.add(i) # 생성자가 있는 숫자들

self_num = sorted(num1 - num2)
for i in self_num:
    print(i)
