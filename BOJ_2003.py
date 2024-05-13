N, M = map(int, input().split())
arr = list(map(int, input().split()))

# Counter Example for num2
# N, M = 4, 9
# arr = [4, 5, 1, 3]

# Answer code
def num1(N, M, arr):
    interval_sum = 0
    end = 0
    count = 0
    for start in range(N):
        while interval_sum < M and end < N: # Consider Escape condition
            interval_sum += arr[end]
            end += 1
        if interval_sum == M:
            count += 1
        interval_sum -= arr[start]
    print(count)

# Wrong code
# If interval_sum == M when the end points last, 
# it cannot enter to while.
# So, the count dropped.
def num2(N, M, arr):
    interval_sum = 0
    end = 0
    count = 0
    for start in range(N):
        while interval_sum <= M and end < N: # Consider Escape condition
            if interval_sum == M:
                count += 1
            interval_sum += arr[end]
            end += 1 
        interval_sum -= arr[start]
    print(count)

num1(N, M, arr)
# num2(N, M, arr)