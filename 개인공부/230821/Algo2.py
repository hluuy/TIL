T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    deck_A = input()
    deck_B = []
    deck_C = []
    bonus = 0
    ssafy_score = 0
    for i in deck_A:
        if i = '+':
            bonus += 1
        elif i.isdecimal():
            draw = int(i) + bonus
            if draw % 2 == 0:
                deck_C.append(draw)
            else:=
                deck_B.append(draw)

    if len(deck_B) < M and len(deck_C) < M:
        print(f'#{t} 0')
        continue
    else:
        for i in range(M-1):
            if len(deck_B) == 0 or len(deck_C) == 0:
                continue
            else:
                deck_B.pop(0)
                deck_C.pop()
    if len(deck_B) >= 1:
        ssafy_score += deck_B[0]
    else:
        pass
    if len(deck_C) >= 1:
        ssafy_score += deck_C[-1]
    else:
        pass

    print(f'#{t} {ssafy_score}')