N = int(input())
time = [0 for _ in range(N)]
pay = [0 for _ in range(N)]
DP = [0 for _ in range(N+1)]

for i in range(N):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    pay[i] = tmp[1]

DP[N] = 0
for i in range(N-1, -1, -1):
    if (N-i) < time[i]:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(pay[i] + DP[i+time[i]], DP[i+1])

print(DP[0])
