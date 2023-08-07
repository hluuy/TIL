T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    total_sum = 0

    for i in range(1, N+1):
        sum_v = lst[0]
        for j in range(1, N+1):
            nj = 0
            nj += i*j
            if 0 <= nj < N:
                a = lst[nj]
                sum_v += a
        total_sum += sum_v
    if total_sum < 0:
        total_sum = 0

    print(f'#{t} {total_sum}')