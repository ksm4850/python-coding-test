while True:
    arr = list(map(int,input().split()))
    arr.sort()
    if sum(arr) == 0:
        break

    if arr[2]**2 == (arr[0]**2) + (arr[1]**2):
        print('right')
    else:
        print('wrong')