square = [list(map(int, input().split())) for _ in range(4)]
cnt = [[0] * 101 for _ in range(101)]
all_square = 0
overlap = 0
last = 0
for idx in range(4):
    x1 = square[idx][0]
    y1 = square[idx][1]
    x2 = square[idx][2]
    y2 = square[idx][3]

    for i in range(x1, x2):
        for j in range(y1, y2):
            if cnt[i][j] != 0: # 비어있지 않다면
                cnt[i][j] = 2
                overlap += 1 # 겹치는 면적의 넓이
            elif cnt[i][j] == 0: # 비어있다면(0이라면)
                cnt[i][j] = 1
                all_square += 1 # 겹치는 면적을 제외한 넓이
            elif cnt[i][j] == 2:
                last += 1
print(all_square)

