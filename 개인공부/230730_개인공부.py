# 문자열 뒤집기
# input : hello world
# a = input()
# b = ''
# for string in a:
#     b = string + b
#
# print(b)

# 문자 갯수 구하기
# input : hello world
# a = input()
# b = 0
# for string in a:
#     if string == 'l':
#         b += 1
# print(b)

# 절대값 구하기
# input : -35
# a = int(input())
#
# if a > 0:
#     b = a
#     print(b)
# else:
#     b = a * (-1)
#     print(b)

# len 구하기
# input : hello world
# a = input()
# b = 0
# for _ in a:
#     b += 1
#
# print(b)

# 문자 위치찾기
# input : hello world
# a = input()
# i = 0
# for string in a:
#     i += 1
#     if string == 'd':
#         print(i-1)
#         break

# 입력 값 더하기
# input : 2 4 5 6 7 8 6
# a = list(map(int, input().split()))
# b = 0
# for num in a:
#     b += num
#
# print(b)

# # set
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# #합집합
# set3 = set()
# for item in set1:
#     set3.add(item)
# for item2 in set2:
#     set3.add(item2)
# print(set3)
# # 차집합
# set3 = set()
# for item in set1:
#     if item not in set2:
#         set3.add(item)
# print(set3)
# # 교집합
# set3 = set()
# for item in set1:
#     if item in set2:
#         set3.add(item)
#
# print(set3)
