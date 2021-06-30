T = int(input())

for _ in range(T):
	cmd = str(input())
	arr_len = int(input())
	arr_ = str(input())
	arr_ = arr_[1:-1].split(',')
	arr = []
	flag = 0
	for i in range(arr_len):
		arr.append(int(arr_[i]))
	start = 0
	end = arr_len -1
	for i in range(len(cmd)):
		if cmd[i] == 'R':
			start, end = end, start
		elif cmd[i] == 'D':
			if len(arr) == 0:
				flag = 1
				break
			if start < end:
				start += 1
			elif start > end:
				start -= 1
			else:
				flag = 1
				break
	if flag == 1:
		print("error")
	else:
		if start > end:
			arr_tmp = arr[end : start + 1]
			arr_tmp.reverse()
			print(arr_tmp)
		elif start < end:
			print(arr[start : end + 1])
		else:
			print("[]")
	arr.clear()
	arr_.clear()
