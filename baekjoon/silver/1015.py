n = int(input())

A = list(map(int,input().split()))

sortA = sorted(A)

P = []

for i in A:
    P.append(sortA.index(i))
    sortA[sortA.index(i)] = -1
    

print(' '.join(map(str,P)))


