'''
1. Cut the tree one meter each
    Max : 1 billion >> 10s

2. Binary search O(logN) >> Max O(log(1B)) >> Good

!! Edge case !!
4 7 
1 1 1 1000000
>> If binary search, when it meets 7 meters, it will end.
However, it is not max heights.
'''

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    cut_heights = 
    if array[mid] == target:
        return target
    elif array[mid] > target:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)

N, M = map(int, input().split())
tree_heights = list(map(int, input().split()))
tree_heights.sort()


    