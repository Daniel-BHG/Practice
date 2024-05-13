# T.C = 0.5M * 0.5M = 0.25e12 ~= 2.5B -> Time out
# Binary search O(logN) = O(12)

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
NL = list(map(int, input().split()))
NL.sort()
M = int(input())
ML = list(map(int, input().split()))
len_NL = len(NL)

for i in ML:
    a = binary_search(NL, i, 0, len_NL-1) 
    if a == None:
        print(0, end = ' ')
    else:
        print(a, end = ' ')
