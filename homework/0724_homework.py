# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(text):
    reversed_text = ''
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

result = reverse_string("Hello, World!")
print(result)

# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(input_list):
    new_lst = []
    for item in input_list:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(input_tuple):
  new_tuple = tuple(sorted(input_tuple))
  return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)

# ws_5_4.py

# 아래 함수를 수정하시오.
def capitalize_words(input_text):
    new_text = input_text.title()
    return new_text


result = capitalize_words("hello, world!")
print(result)

# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(numbers):
    result = []
    while numbers:
        number = numbers.pop(0)
        if number % 2 == 0:
            result.extend([number])
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

# main.py

# 아래 함수를 수정하시오.
def count_character(a, b):
    count_num = int(a.count(b))
    return count_num



result = count_character("Hello, World!", "o")
print(result) # 2

# main.py

# 아래 함수를 수정하시오.
def find_min_max(input_list):
    input_list.sort()
    max_num = max(input_list)
    min_num = min(input_list)
    result = (min_num, max_num)
    return result

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
