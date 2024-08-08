"""
input 1 일경우 0
(x 최대값 - x 최소값) * (y 최대값 - y 최소값) 

"""


N = int(input())

x_list,y_list = [],[]
for i in range(N):
    x, y = map(int,input().split())

    x_list.append(x)
    y_list.append(y)

print((max(x_list)-min(x_list)) * (max(y_list)-min(y_list)))