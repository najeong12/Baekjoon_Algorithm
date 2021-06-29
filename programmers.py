N, number = map(int, input().split())

dp = [set() for _ in range(9)]
dp[0].add(N)

for idx in range(1, 9):
	dp[idx].add(int(str(N) * idx))
	for tmp in range(1, idx):
		for a in range(len(dp[tmp])):
			for b in range(len(dp[idx - tmp])):
				dp[idx].add(a+b)
				dp[idx].add(a-b)
				if (b):
					dp[idx].add(int(a/b))
				dp[idx].add(int(a*b))
				if number in dp[idx]:
					print(idx+1)