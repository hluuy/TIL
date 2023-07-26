# ws_6_1.py

# 아래 함수를 수정하시오.
def union_sets(a, b):
    result = a.union(b)
    return result

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)

# ws_6_2.py

# 아래 함수를 수정하시오.
def get_value_from_dict(input_dict):
    result = input_dict.get('name')
    return result

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict)
print(result) # Alice

# ws_6_3.py

# 아래 함수를 수정하시오.
def intersection_sets(a, b):
    result = a.intersection(b)
    return result

result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result) # {3}

# ws_6_4.py

# 아래 함수를 수정하시오.
def get_keys_from_dict(input_dict):
    input_keys = input_dict.keys()
    result = list(map(str, input_keys))
    
    return result

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)

# ws_6_5.py

# 아래 함수를 수정하시오.
def difference_sets(a, b):
    result = a.difference(b)
    return result

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)

# hw_6_2.py

# 아래 함수를 수정하시오.
def remove_duplicates_to_set(input_list):
    fix_list = []
    for item in input_list:
        if item not in fix_list:
            fix_list.append(item)
    
    result_set = set(fix_list)
    return result_set


		
result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(input_dict):
    new_dict = input_dict.copy()
    new_dict.update(country = 'USA')
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict)
print(result)
