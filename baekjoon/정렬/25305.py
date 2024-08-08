"""
N명의 학생 중 k명은 상을받음
"""
N, k = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

print(arr[k-1])