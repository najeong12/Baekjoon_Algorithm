arr = []
N = int(input())

for i in range(N):
	cmd = int(input())
	if cmd != 0:
		arr.append(cmd)
	else:
		if len(arr) == 0:
			print(0)
		else:
			print(max(arr))
			arr.remove(max(arr))