"""
A : 낮에 올라가는 미터
B : 떨어지는 미터
V : 나무높이

며칠걸리는지 계산

(V-B)/(A-B)
후 반올림

"""
import math
A, B, V = map(int,input().split()) 
day = (V-B)/(A-B)
print(math.ceil(day))