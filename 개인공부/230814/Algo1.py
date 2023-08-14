T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    for i in range(N):
        for j in range(N):
            a = lst[i][j]
            max_s = 0
            for p in range(4):
                ni, nj = i+di[p], j+dj[p]
                if 0 <= ni < N and 0 <= nj < N:
                    s = lst[ni][nj]
                    if max_s < s:
                        max_s = s
                        
            if a > max_s:
                cnt += 1

    print(f'#{t} {cnt}')