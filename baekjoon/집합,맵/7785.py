import sys

input = sys.stdin.readline

n = int(input())

dic = dict()
for _ in range(n):
    name, stat = map(str,input().strip().split())
    if stat == 'enter':
        dic[name] = stat
    elif stat == 'leave':
        del dic[name]


for i in sorted(dic.keys(),reverse=True):
    print(i)