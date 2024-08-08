"""
파이썬의 round는 오사오입

사사오입
4 이하의 숫자는 내림, 5 이상의 숫자는 올림

오사오입
5 미만의 숫자는 내림, 5초과의 숫자는 올림
반올림할 자릿수가 5면 5의 앞자리가 홀수인경우 올림, 짝수인경우 내림
값에 0.5를 더한후 int()를 적용
"""
def my_round(val):
    if val - int(val) >= 0.5:
        return int(val)+1
    else:
        return int(val)
import sys
input = sys.stdin.readline

n = int(input())

arr = []
if n != 0:
    for _ in range(n):
        arr.append(int(input()))

    arr.sort()

    a = my_round(n * 0.15)

    if a > 0:
        print(my_round(sum(arr[a:-a])/len(arr[a:-a])))
    else:
        print(my_round(sum(arr)/len(arr)))
else:
    print(0)

print(avg)
