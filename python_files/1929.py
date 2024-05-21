'''
에라토스테네스의 채 T.C = O(N log log N) ~= O(N)
1. Set all nums in list as True
2. If the num in list is True, set the multiplied nums as False
3. Print all true nums
'''

import math

a, b = input().split()
a, b = int(a), int(b)

nums = [True for _ in range(b+1)] # Set all nums as True
nums[1] = False # 1 is False always
# nums = [T0, T1, T2 ..., Tb]

for i in range(2, int(math.sqrt(b))+1): # Filtering
    if nums[i] == True:
        j = 2
        while i*j <= b:
            nums[i*j] = False
            j += 1
# nums = [T0, T1, T2, T3, F4, T5, F6, ... ?b]

for i in range(a, b+1): # Print
    if nums[i]:
        print(i)
