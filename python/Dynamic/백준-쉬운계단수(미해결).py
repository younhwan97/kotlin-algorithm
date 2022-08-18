import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 101
dp[1] = 9
dp[2] = 17

for i in range(3, len(dp)):
    ## dp[1]
    ## 1, 2, 3, 4, 5, 6, 7, 8, 9

    ## dp[2]
    ## 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98

    ## dp[3]
    ## 101, 121, 123, 210, 212, 232, 234, 321, 323, .... 987, 989
    dp[i] = (dp[i - 1] * 2 - 1) % 1_000_000_000

print(dp[n])