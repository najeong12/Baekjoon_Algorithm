# str1 = input()
# str2 = input()

# arr = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
# for i in range(1, len(str1) + 1):
# 	for j in range(1, len(str2) + 1):
# 		if str1[i-1] == str2[j-1]:
# 			arr[i][j] = arr[i-1][j-1] + 1
# 		else:
# 			arr[i][j] = max(arr[i][j-1], arr[i-1][j])
# 		print(arr)
# print(arr[-1][-1])

import sys
S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
	for j in range(1, len2 + 1):
		if S1[i - 1] == S2[j - 1]:
			matrix[i][j] = matrix[i - 1][j - 1] + 1
		else:
			matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
			
print(matrix[-1][-1])
