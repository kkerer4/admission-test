def count(input):
  count_dict = {}
  for char in input:
      if char in count_dict:
          count_dict[char] += 1
      else:
          count_dict[char] = 1
  return count_dict
    
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

def group_by_key(input):
  result_dict = {}
  for item in input:
      key = item['key']
      value = item['value']
      if key in result_dict:
          result_dict[key] += value
      else:
          result_dict[key] = value
  return result_dict

input2 = [
{'key': 'a', 'value': 3}, {'key': 'b', 'value': 1}, {'key': 'c', 'value': 2}, {'key': 'a', 'value': 3}, {'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
