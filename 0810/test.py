N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열 원소들의 합을 구할 수 있는가?

s = 0

for i in range(N):
    for j in range(N):
        s += arr[i][j]

print(s)

