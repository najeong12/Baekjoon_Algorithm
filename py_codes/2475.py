arr = list(map(int, input().split()))
answer = 0
for i in range(5):
	answer += arr[i] * arr[i]
print(answer % 10)