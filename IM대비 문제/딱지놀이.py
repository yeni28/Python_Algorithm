N = int(input())
for i in range(N):
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_pic_num = a_list[0]
    b_pic_num = b_list[0]

    for a in range(a_pic_num[0]):
        if a_list[a+1] == 4:
            w