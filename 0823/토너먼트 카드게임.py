# 카드게임 분할정복 함수
# i, j : i번째 학생부터 j번째 학생까지
def tournament(i, j):
    if i == j:
        #i랑 j가 같으면 둘로 쪼개는 게 불가능하다.
        return i

    # 분할이라는 단계를 어떻게 할 것인가?
    # 나누는 기준 left = i ~ (i+j)//2 ...

    #분할을 먼저 해볼 것이다.
    # 재귀함수를 이용해서 풀 것
    else:
    # 왼쪽과 오른쪽을 나누는 일을 계속 반복적으로 하니까 재귀함수로 만들자
        left = tournament(i, ((i + j)//2)) # 왼쪽 쪼개기
        right = tournament(((i+j)//2) + 1, j) # 오른쪽 쪼개기
        return winner(left, right) #left 와 right 중 승자를 구해 리턴

    # 왼쪽과 오른쪽 중에 승자를 정한다.
    # 승자의 인덱스를 리턴 하도록 한다.

def winner(left, right):

        if card_list[left-1] == card_list[right-1]:
            if left-1 < right-1:
                return left
            else:
                return right

        elif card_list[left-1] == 1:
            if card_list[right-1] == 2:
                return right
            elif card_list[right-1] == 3:
                return left

        elif card_list[left-1] == 2:
            if card_list[right-1] == 1:
                return left
            elif card_list[right-1] == 3:
                return right

        elif card_list[left-1] == 3:
            if card_list[right-1] == 1:
                return right
            elif card_list[right-1] == 2:
                return left

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
    result = tournament(1, N)
    print(f'#{tc} {result}')


