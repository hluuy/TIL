# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[0]
    min_value = arr[0]
    for i in range(1, N):
        if max_value < arr[i]:
            max_value = arr[i]
        if min_value > arr[i]:
            min_value = arr[i]

    ans = max_value - min_value

    print(f'#{tc} {ans}')