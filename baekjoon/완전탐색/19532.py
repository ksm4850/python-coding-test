"""
ax + by = c 
dx + ey = f

1x + 3y = -1 
4x + 1y = 7

(-1 * 1 - 3 * 7) //(1 * 1 - 3 * 4)
"""

a,b,c,d,e,f = map(int,input().split())
# print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))
for x in range(-999,1000):
    for y in range(-999,1000):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x,y)
            break