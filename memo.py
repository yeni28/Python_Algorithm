N = int(input())
num_list = list(map(int, input().split()))

min_n = 1000000
max_n = 0

for i in range(N):
    if num_list[i] > max_n:
        max_n = num_list[i]
for j in range(N):
    if num_list[j] < min_n:
        min_n = num_list[j]

print(f'{min_n} {max_n}')