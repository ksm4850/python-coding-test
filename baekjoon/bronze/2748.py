def fibo(n):
    arr = [1,1]
    if n == 0:
        return 0
    if n <= 2:
        return arr[n-1]
    
    for i in range(2,n):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n-1]

print(fibo(int(input())))