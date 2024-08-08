text = str(input())

T = ['c=','c-','dz=','d-','lj','nj','s=','z=']

result = len(text)
for i in T:
    result -= text.count(i)

print(result)
