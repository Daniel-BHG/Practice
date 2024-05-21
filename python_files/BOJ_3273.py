'''
Counter Examples
    - 1 1 1 1 1 1 1 1 1 >> The pair doesn't exist
    - x x x x+1 .. >> No case

Max number of len(arr) = 100,000

1. Simple Brute Force
    - Max T.C = 99,999 + 99,998 + ... + 2 + 1 = 100,000 * 50,000 = 5,000,000,000 = 5B ~= 50s

2. After sorting
    1 2 3 5 7 9 10 11 12
    - It would be better, but what if...
    1 1 1 1 1 1 1 1 1 1 .. for 100,000 times
    and if all cases doesn't meet the condition?


...After Hint...
1. Using Hash map.
    Check possible cases and find if the target number is there.
    O(N)

2. Using upgraded two pointer. Sorting and check start from 1st and last number. 
    If sum > x, right pointer -= 1
    If sum < x, left pointer += 1
    Sort O(NlogN)
    Check O(N)
'''

##### 2. Upgraded two pointer #####
def upgraded_two_pointer():
    arr.sort()
    lenarr = len(arr)
    start = 0
    end = lenarr-1
    count = 0

    while start < end:
        sum = arr[start] + arr[end]
        if sum > x:
            end -= 1
        elif sum < x:
            start += 1
        else: # sum == x
            count += 1
            start += 1
    print(count)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

upgraded_two_pointer()