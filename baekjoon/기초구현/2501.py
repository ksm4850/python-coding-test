n,k = map(int, input().split())

num_list = []
for i in range(1, n//2+1):
    if n%i == 0:
        num_list.append(i)

num_list.append(n)

if k > len(num_list):
    print(0)
else:
    print(num_list[k-1])