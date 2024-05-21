'''
백준 11053 가장 긴 증가하는 부분 수열

dp[-1]과 비교해서 크면 dp 저장

Edge case 
20 10 10 20 30 40 -> 20으로 시작할 경우..
20 30 40 50 10 20 -> 무조건 작은거로 시작해야 하는건 아님

모든 경우 체크할 시 T.C = 1000 + 999 + ... + 2 + 1 = 1001 * 500 = 500,000 < 1s

6
10 20 10 30 20 50
1 
-> 4

6
20 10 10 20 30 40
1 1 1 2 3 4
-> 4

6
20 30 40 50 10 20
1 2 3 4 4 4
1 2 3 4 1 2
-> 4

6
10 100 20 30 40 50
1 2 2 3 4 5
-> 5
'''

N = int(input())
arr = list(map(int, input().split()))
cnt_list = []
len_arr = len(arr)
dp = {value:0 for value in arr}
cnt = 1
dp.append(cnt)

for i in range(1, len_arr):
    if arr[i] > 


for i in range(len_arr):
    cnt = 1
    # dp = list(0 for _ in range(N)) # Initialize
    dp = arr[i]
    for j in arr[i+1:]:
        if j > dp:
            cnt += 1
            dp = j
    cnt_list.append(cnt)
print(cnt_list)
print(max(cnt_list))