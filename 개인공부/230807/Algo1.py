T = int(input())
for t in range(1, T+1):
    N = int(input())
    area = list(map(int, input().split()))
    background = [list(map(int, input().split()))for _ in range(N)]
    x1 = area[0]
    y1 = area[1]
    x2 = area[2]
    y2 = area[3]
    sum_v = 0
    count = 0
    avg_v = 0
    flatten = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            a = background[i][j]
            sum_v += a
            count += 1
    avg_v = sum_v // count
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if 0 < background[i][j] < avg_v:
                flatten += avg_v - background[i][j]
            elif background[i][j] == avg_v:
                pass
            elif background[i][j] > avg_v:
                flatten += background[i][j] - avg_v

    print(f'#{t} {flatten}')