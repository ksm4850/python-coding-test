a,b = map(str,input().split())

a,b = a.replace('6','5'), b.replace('6','5')
min = int(a)+int(b)
a,b = a.replace('5','6'), b.replace('5','6')
max = int(a)+int(b)
print(min,max)