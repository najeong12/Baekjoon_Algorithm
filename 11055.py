import sys
input = sys.stdin.readline

def find_prev(i, arr, dp):
    tmp=[]
    for j in range(i):
        if (arr[j] < arr[i]):
            tmp.append(dp[j])
    if (len(tmp)==0):
        return -1
    return dp.index(max(tmp))

n = int(input())
arr = list(map(int, input().split()))

dp = [0]*(n+1)
dp[0] = arr[0]
for i in range(1, n):
    if (find_prev(i, arr, dp) != -1):
        dp[i] = dp[find_prev(i, arr, dp)] + arr[i]
    else:
        dp[i] = arr[i]

print(max(dp))