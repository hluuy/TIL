T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    count = 0
    max_v = 0
    for i in range(N):
        for j in range(N):
            a = MAP[i][j]
            if ((N - 1) - i + 1) * ((N - 1) - j + 1) < max_v:
                break
            for p in range(i, N):
                for q in range(j, N):
                    s = MAP[p][q]
                    if a == s:
                        size = (p - i + 1) * (q - j + 1)
                        if max_v < size:
                            max_v = size
                            count = 1
                        elif max_v == size:
                            count += 1
    print(f'#{t} {count}')