T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 1, 1, N-1]
    dj = [1, 1, 0, N-1, 1]
    count = 0
    max_v = 0
    for i in range(N):
        for j in range(N):
            a = MAP[i][j]
            for p in range(5):
                for q in range(N):
                    ni, nj = i + di[p] * q, j + dj[p] * q
                    if i <= ni < N and j <= nj < N:
                        s = MAP[ni][nj]
                        if a == s:
                            if max_v < (ni - i + 1) * (nj - j + 1):
                                max_v = (ni - i + 1) * (nj - j + 1)
                                count = 1
                                continue
                            if max_v == (ni - i + 1) * (nj - j + 1):
                                count += 1

    print(f'#{t} {count}')
