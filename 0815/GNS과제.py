
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline #상위 단계에서 전체를 읽어옴

T = int(input().rstrip()) #/n을 지워주기 위해 rstrip 사용
number_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'] #리스트의 인덱스와 그 값으로 카운팅 정렬을 이용
for tc in range(1, T+1):
    order, n = input().split()
    arr = list(input().split())

    cnt = [0] * 10

    for idx in arr:
        for j in range(len(number_list)):
            if idx == number_list[j]:
                cnt[j] += 1


    print(f'#{tc}')

    for idx in range(10): #num_list와 cnt의 인덱스는 공통!
        print((number_list[idx] + ' ') * cnt[idx], end='')

