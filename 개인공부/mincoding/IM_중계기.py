T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(N + 1)]
    calc = []
    max_distance = 0
    for i in range(N+1):
        for j in range(N+1):
            if MAP[i][j] == 2:
                row, col = i, j
            if MAP[i][j] == 1:
                calc.append([i, j])
    for point in calc:
        distance = ((point[0] - row)**2 + (point[1] - col)**2)**0.5
        max_distance = max(max_distance, distance)
        if max_distance % 1 > 0:
            max_distance = max_distance // 1 + 1
    print(f'#{t} {int(max_distance)}')
    # for i in range(len(calc)):
    #     # if max_row_d < abs(calc[i][1] - col):
    #     #     max_row_d = abs(calc[i][1] - col)
    #     # if max_col_d < abs(calc[i][0] - row):
    #     #     max_col_d = abs(calc[i][0] - row)
    #     max_row_d = max(max_row_d, abs(calc[i][1] - col))
    #     max_col_d = max(max_col_d, abs(calc[i][0] - row))
    # print(max(max_col_d, max_row_d))