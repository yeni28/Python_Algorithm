

T = int(input())

for case in range(1, T+1):
    N = int(input())
    cards = input()

    card_count = [0] * 10
    for card in cards:
        card_count[int(card)] += 1

    max_card = 0
    max_num = 0

    for i in range(len(card_count)): #card count의 index를 뽑아온다.
        if max_card <= card_count[i]:
            max_card = card_count[i]
            max_num = i

    print(f'#{case} {max_num} {max_card}')


