arr = [7,2,5,3,4,3]

N = len(arr)

for i in range(N-1):
    minIdx = i #구간의 맨 앞 값을 최소값으로 가정
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
        arr[minIdx], arr[i] = arr[i], arr[minIdx] #최소값을 구간 맨 앞으로

print(arr)