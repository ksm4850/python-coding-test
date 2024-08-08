# O(N^2) 시간복잡도

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))


# arr = sorted(arr)
# arr.sort()

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1], arr[j]
        print(arr)
        
# for i in arr:
#     print(i)


