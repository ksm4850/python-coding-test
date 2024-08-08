lines= []
length = [] 
ans = ''
for _ in range(5):
    line=input()
    length.append(len(line))
    lines.append(line)

for j in range(max(length)):
    for i in range(5):
        if j< length[i]:
            ans+=lines[i][j]

print(ans)