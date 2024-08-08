S = str(input())
total = set()
for i in range(len(S)):
    for j in range(i,len(S)):
        print(S[i:j+1])
        total.add(S[i:j+1])

print(len(total))