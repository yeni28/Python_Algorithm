K = int(input())
max_width = 0
min_width = 5000
max_height = 0
min_height = 5000

for i in range(6):
    di, le = map(int, input().split())
    if di == 1 or di == 2:
        if le > max_width:
            max_width = le
        if le < min_width:
            min_width = le
    elif di == 3 or di == 4:
        if le > max_height:
            max_height = le
        if le < min_height:
            min_height = le

a1 = max_width * max_height
a2 = min_width * min_height

print(K * (a1 - a2))

