#  # def max_value(row, col):
# # #     global h
# # #     max_v = 0
# # #     # result_def = 0
# # #     #
# # #     # lastest = []
# # #     while len(visited) != 5:
# # #         # can_lst = []
# # #         for p in range(8):
# # #             ni, nj = row + di[p], col + dj[p]
# # #             if 0 <= ni < H and 0 <= nj < W:
# # #                 # if a != MAP[ni][nj] and value < MAP[ni][nj]:
# # #                 #     q = MAP[ni][nj]
# # #                 #     value += q
# # #                 s = MAP[ni][nj]
# # #                 if max_v < s:
# # #                     max_v = s
# # #
# # #                 return max_value(ni, nj)
# #         #         if s not in lastest:
# #         #             can_lst.append(s)
# #         #             lastest.append(max(can_lst))
# #         # result_def += max(can_lst)
# #                 # if s not in lastest and max_v < s:
# #                 #     max_v = s
# #                 #     lastest.append(max_v)
# #                 # result_def += max_v
# #
# #
# di = [0, 1, 1, 1, 0, -1, -1, -1]
# dj = [1, 1, 0, -1, -1, -1, 0, 1]
#
# def max_value(row, col):
#     max_s = 0
#     while len(lst) < 5:
#         for p in range(8):
#             ni, nj = row + di[p], col + dj[p]
#             if 0 <= ni < H and 0 <= nj < W:
#                 s = MAP[ni][nj]
#                 if max_s < s and s not in lst:
#                     max_s = s
#                     lst.append(s)
#                     max_value(ni, nj)
#     return
#
# T = int(input())
# for t in range(1, T + 1):
#     h = 0
#     W, H = map(int, input().split())
#     MAP = [list(map(int, input().split()))for _ in range(H)]
#
#     result = 0
#     lst = []
#     max_a = 0
#
#
#     for i in range(H):
#         for j in range(W):
#             a = MAP[i][j]
#             if max_a < a:
#                 max_a = a
#     lst.append(max_a)
#     for i in range(H):
#         for j in range(W):
#             a = MAP[i][j]
#             if a == max_a:
#                 max_value(i, j)
#
#     lst.sort()
#     print(f'#{t} {sum(lst[-4:])**2}')
# #
# #                 # max_value(i, j)
# #
# #
# #             # for p in range(8):
# #             #     ni, nj = i + di[p], j + dj[p]
# #             #     if 0 <= ni < H and 0 <= nj < W:
# #             #         if a != MAP[ni][nj] and s < MAP[ni][nj]:
# #             #             s = MAP[ni][nj]
# #             # if max_v < s:
# #             #     max_v = s
# #     print(max_a)
# # T = int(input())
# # for t in range(1, T + 1):
# #     h = 0
# #     W, H = map(int, input().split())
# #     MAP = [list(map(int, input().split()))for _ in range(H)]
# #     max_v = 0
# #     for i in range(H):
# #         for j in range(W):
# #             s = 0
# #             for p in range(2):
# #                 for q in range(2):
# #                     s += MAP[p][q]
# #             if max_v < s:
# #                 max_v = s

def sum_value(x, y, n, s, v):
    if n == 3:
        SUM.add(s)
        return
    if y % 2 == 0:
        d = d1
    else:
        d = d2
    for i in range(6):
        dx = x + d[i][0]
        dy = y + d[i][1]
        if 0 <= dx < H and 0 <= dy < W and v[dx][dy] == 0:
            v[dx][dy] = 1
            sum_value(dx, dy, n + 1, s + lst[dx][dy], v)
            v[dx][dy] = 0


d1 = [(-1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
d2 = [(0, -1), (0, 1), (1, 0), (1, -1), (1, 1), (-1, 0)]
T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(H)]
    SUM = set()
    v = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            v[i][j] = 1
            sum_value(i, j, 0, lst[i][j], v)
            v[i][j] = 0
            if j % 2 == 0:
                d = d1
            else:
                d = d2
            for k in range(2):
                value = lst[i][j]
                for l in range(3):
                    di = i + d[3 * k + l][0]
                    dj = j + d[3 * k + l][1]
                    if 0 <= di < H and 0 <= dj < W:
                        value += lst[di][dj]
                SUM.add(value)
    result = (max(SUM))
    print(f'#{t + 1}', result)