N = int(input())
num_list = list(map(int, input().split()))

min_n = 1000000
max_n = 0
for i in range(len(num_list)):
    if num_list[i] > max_n:
        max_n = num_list[i]
    elif num_list[i] < min_n:
        min_n = num_list[i]

print(min_n, max_n)