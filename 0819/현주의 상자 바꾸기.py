T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for num in range(L-1, R):
            box[num] = i

    box_num = ""
    for j in box:
        box_num += str(j) + " "

    print(f'#{tc} {box_num}')
