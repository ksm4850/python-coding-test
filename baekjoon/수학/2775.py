import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    # k 층 n 호

    arr = [ i for i in range(1,num+1)] # 0층 리스트

    for k in range(floor): # 층수만큼 반복
        for i in range(1, num): 
            arr[i] += arr[i-1] # 층별 각 사람 수 변경
    print(arr[-1])