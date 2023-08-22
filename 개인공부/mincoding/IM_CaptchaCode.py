T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))
    passcode_lst = []
    for item in passcode:
        passcode_lst.append(item)
    result = []

    for i in range(N):
        if len(passcode_lst) >= 1 and len(sample) >= 1:
            if passcode_lst[0] != sample[0]:
                sample.pop(0)
            elif passcode_lst[0] == sample[0]:
                sample.pop(0)
                result.append(passcode_lst.pop(0))
    if passcode == result:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
    # sample_lst = []
    # passcode_lst = []
    # final_passcode = []
    # result = []
    # for item in sample:
    #     if item.isdecimal():
    #         sample_lst.append(int(item))
    # for item in passcode:
    #     if item.isdecimal():
    #         passcode_lst.append(int(item))
            # final_passcode.append(int(item))
    # for i in range(N):
    #     if len(passcode_lst) >= 1 and len(sample_lst) >= 1:
    #         if passcode_lst[0] != sample_lst[0]:
    #             sample_lst.pop(0)
    #         elif passcode_lst[0] == sample_lst[0]:
    #             sample_lst.pop(0)
    #             result.append(passcode_lst.pop(0))
    #
    # if final_passcode == result:
    #     print(f'#{t} 1')
    # else:
    #     print(f'#{t} 0')
    # print(sample)
    # print(passcode)
    # print(passcode_lst)