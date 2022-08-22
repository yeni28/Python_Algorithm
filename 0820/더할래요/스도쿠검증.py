def sudoku():
    # 행 탐색
    for i in range(9):
        num_list = []
        for j in range(9):
            if arr[i][j] not in num_list:
                num_list += [arr[i][j]]
        if len(num_list) != 9:
            return 0

    # 열 탐색
    for j in range(9):
        num_list = []
        for i in range(9):
            if arr[i][j] not in num_list:
                num_list += [arr[i][j]]
        if len(num_list) != 9:
            return 0

        # 박스 탐색
    for j in range(0, 9, 3):
        for i in range(0, 9, 3):
            num_list = [] # 박스 범위 오류 체크
            for m in range(3):
                for k in range(3):
                    if arr[i + m][j + k] not in num_list:
                        num_list += [arr[i + m][j + k]]
            if len(num_list) != 9:
                return 0
    return 1



T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    #가로 9칸 세로 9칸을 탐색하며 같은 숫자가 있는지 확인
    #추가로 3x3 까지 확인


    print(f'#{tc} {sudoku()}')

