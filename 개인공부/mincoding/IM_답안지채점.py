T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    lst = [list(map(int, input().split()))for _ in range(N)]
    scores = []
    for i in range(N):
        score = 0
        bonus = 0
        for j in range(M):
            if lst[i][j] == ans[j]:
                score += 1 + bonus
                bonus += 1
            else:
                bonus = 0
        scores.append(score)
    result = max(scores) - min(scores)
    print(f'#{t} {result}')

# 이건 왜 안됨
# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     ans = list(map(int, input().split()))
#     lst = [list(map(int, input().split()))for _ in range(N)]
#     scores = []
#     for i in range(N):
#         score = 0
#         bonus = 0
#         for j in range(M):
#             if bonus > 0:
#                 score += bonus
#             if lst[i][j] == ans[j]:
#                 score += 1
#                 bonus += 1
#             else:
#                 bonus = 0
#         scores.append(score)
#     result = max(scores) - min(scores)
#     print(f'#{t} {result}')
