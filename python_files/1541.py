'''
1. Appending numbers and +, -

2. If +, 
    calculate A + B
    remove related elements

3.Calculate minus

** Runtime Error
- What if the start letter is zero?
'''

### No. 1 ###
line = input()
lst_line = []

num = ''
for char in line:
  if char in '+-':
    lst_line.append(int(num))
    lst_line.append(char)
    num = ''
  else:
    num += char
lst_line.append(int(num))  # last number

### No. 2 ###
# Plus operation revertly for avoiding index error
# 1-3+5-2+7
# [1, -, 3, +, 5, -, 2, +, 7]
# [1, -, 3, +, 5, -, 9]
i = len(lst_line) - 1
while i > 0:
  if lst_line[i] == '+':
    lst_line[i - 1] += lst_line[i + 1]
    i -= 1
    del lst_line[i + 1:]  # delete until next minus
  else:
    i -= 1
# [10, '-', 13, '-', 43]

### No. 3 ###
# Minus operation
# [10, '-', 13, '-', 43]
# [10, '-', -3, '-', 43]
# [10, '-', -3, '-', -46]
j = 0
while j < len(lst_line) - 1:
  if lst_line[j] == '-':
    lst_line[j + 1] = lst_line[j - 1] - lst_line[j + 1]
    j += 1
  else:
    j += 1

print(lst_line[-1])
'''
Index error code

##### No. 1 #####
# ref_idx = 0
# for idx, elem in enumerate(line):
#     if elem in '+-':
#         lst_line.append(line[ref_idx:idx]) # number
#         lst_line.append(line[idx:idx+1]) # plus, minus
#         ref_idx = idx + 1

#     # Store last number
#     elif line[ref_idx:].count("+") + line[ref_idx:].count("-") == 0: # avoid meaningless elements
#         if not lst_line[-1].isdigit(): # avoid duplicated same last number
#             lst_line.append(line[ref_idx:])

##### No. 2 #####
# # ['0001', '-', '59', '+', '38', '+', '49']
# for idx, elem in enumerate(lst_line):
#     if (elem == "+"):
#         temp_sum = str(int(lst_line[idx-1]) + int(lst_line[idx+1]))
#         # del lst_line[idx-1:idx+2]
#         lst_line[idx-1] = 0 # because hard to control idx if delete
#         lst_line[idx+1] = temp_sum
#         # ['0001', '-', 0, '+', '97', '+', '49']
#         # ['0001', '-', 0, '+', 0, '+', '146']

# # ['0001', '-', 0, '+', 0, '+', '146']
# # ['0', '-', 0, '+', '2']
# # Remove 0, '+'
# while lst_line.count(0) > 0:
#     lst_line.remove(0)
# while lst_line.count('+') > 0:
#     lst_line.remove('+')


##### No. 3 #####
# # ['0', '-', '2']
# # ['0001', '-', '146'] -> -145
# # Also consider ['0001', '-', '30', '-', '73']
# for idx, elem in enumerate(lst_line):
#     if elem == '-':
#         temp_sub = int(lst_line[idx-1]) - int(lst_line[idx+1])
#         lst_line[idx-1] = 0
#         lst_line[idx+1] = temp_sub
#         # ['0', '-', '-29', '-', '73']
#         # ['0', '-', 0, '-', -102]
# print(lst_line[-1]) # It is okay if there is only pluses

'''
