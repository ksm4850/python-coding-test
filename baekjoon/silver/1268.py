n = int(input())

ban = [] # 학생별 1~5학년까지 속했던 반
same = [0] * n # 행 번 학생이 열 번 학생과 같은반이었는지 여부

for i in range(n):
    ban.append(list(map(int,input().split())))
    same[i] = [0] * n

for  i in range(5): # i 학년
    for j in range(n): # j번의 i 학년
        for k in range(j+1,n): # k번의 i 학년비교
            if ban[j][i] == ban[k][i]:
                same[k][j] = 1
                same[j][k] = 1
cnt = []
for s in same:
    cnt.append(s.count(1))
print(cnt.index(max(cnt)) + 1)
