'''
4
1 3 1 5

7
1 3 1 5 2 6 5
'''
# 1 3 1 5 2 6 5
# 1 3 3 8 8 14 14
N = int(input())
K = list(map(int, input().split()))

dp = list(0 for _ in range(N))

dp[0] = K[0]
dp[1] = max(K[0], K[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+K[i])
print(dp)
print(max(dp)) # or print(dp[-1])