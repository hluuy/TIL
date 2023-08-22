T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0
    for i in range(N):
        for j in range(N):
            a = MAP[i][j]
            s = 0
            for p in range(4):
                for q in range(1, P + 1):
                    ni, nj = i + di[p] * q, j + dj[p] * q
                    if 0 <= ni < N and 0 <= nj < N:
                        s += MAP[ni][nj]
            if max_v < a + s:
                max_v = a + s

    print(f'#{t} {max_v}')