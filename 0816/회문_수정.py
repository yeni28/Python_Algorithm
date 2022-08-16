T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    # nxn의 글자 받기
    arr = [list(input()) for _ in range(n)]
#회문 찾기, 가로 및 세로, 회문의 개수는 1개
# arr은 [['GOFFAKWFSM'], ['OYECRSLDLQ'] ...] 형태
    # 수정 후 > [['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M'], ['O', 'Y', 'E', 'C', 'R', 'S', 'L', 'D', '
# 문자열을 배열로 만들고 싶은데 방법을 잘 모르겠음 /
    # split을 써서 띄어쓰기가 없어서 그런것이었음! 지우니까 해결

    # 가로 회문 탐색
    # for i in arr:
    #     reverse_str = ""
    #     compare_str = ""
    #     for j in range(m-1, -1, -1):
    #         reverse_str += i[j]
    #     for k in range(m):
    #         compare_str += i[k]
    #
    #     if reverse_str == compare_str:
    #         result = reverse_str
    #         print(result)

    # 세로 회문 탐색
    # 1열부터 차례대로 이어져서 출력되고 있는 상황
    # n개까지만 출력되고 다시 새롭게 리스트에 추가하는 방법이 뭘까?

    list1 = []
    for i in range(n):
        for c in range(n):
            list1 += arr[c][i]
            new_list = [list1 for _ in range(n)]
    # print(list1)
    print(new_list)

    # for i in new_list:
    #     reverse_str = ""
    #     compare_str = ""
    #     for j in range(m-1, -1, -1):
    #         reverse_str += i[j]
    #     for k in range(m):
    #         compare_str += i[k]
    #
    #     if reverse_str == compare_str:
    #         result = reverse_str
    #         print(result)

    # print(f'#{tc} {result}')