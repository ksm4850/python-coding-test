"""
규칙
1/1
1/2, 2/1
3/1, 2/2, 1/3
1/4, 2/3, 3/2, 4/1
5/1, 4/2, 3/3, 2/4, 1/5

짝수라인 분모가 1씩 늘어나고 분자가 1씩 줄어듬
홀수라인 분자가 1씩 늘어나고 분모가 1씩 줄어듬
"""

num = int(input())
line = 1
while num > line:
    num -= line
    line += 1

# print(f"num : {num}  line : {line}")

# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f"{a}/{b}")
