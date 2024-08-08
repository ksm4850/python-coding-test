# O(N^2) 시간복잡도
# 배열이 역순으로 정렬되어있는 경우, 각 원소를 삽입할때마다 이동이 필요
array = [5,3,4,2,1]
for i in range(1, len(array)):
    for j in range(i, 0, -1): 
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
    
