T = int(input())
for t in range(1, T + 1):
    lst = list(input())
    new_lst = []
    stack = []
    for i in lst:
        if i in '(){}':
            stack.append(i)
            if len(stack) > 1:
                if (stack[-1] == ')' and stack[-2] == '(') or (stack[-1] == '}' and stack[-2] == '{'):
                    stack.pop()
                    stack.pop()
    if len(stack) > 1:
        print(f'#{t} -1')

    else:
        for i in lst:
            if i in "(){}":
                new_lst.append(i)
            elif i not in "(){}":
                new_lst.append(int(i))
        if type(new_lst[0]) == int:
            print(f'#{t} -1')

