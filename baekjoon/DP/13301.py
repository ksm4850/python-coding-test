def dp(num):
    arr = [4,6]

    for i in range(2,num):
        arr.append(arr[i-1] + arr[i-2])
    
    return arr[num-1]

n = int(input())
print(dp(n))