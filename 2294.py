import sys
input = sys.stdin.readline

def nj(k, arr, dp):
    temp=[]
    for i in arr:
        if k >= i and dp[k-i] != -1:
            temp.append(dp[k-i]+1)

    if len(temp)>0:
        return min(temp)
    else:
        return -1

n, k = map(int, input().split())
arr=[]

for i in range(n):
    arr.append(int(input()))
arr.sort()

dp = [-1 for i in range(k + 1)]

for i in range(1, k+1):
    if i in arr:
        dp[i] = 1
    else:
        dp[i] = nj(i, arr, dp)
    
print(int(dp[k]))