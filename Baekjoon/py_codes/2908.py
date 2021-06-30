A, B = map(int, input().split())
a = 0
b = 0
for i in range(3):
	a = (a * 10) + (A % 10)
	b = (b * 10) + (B % 10)
	A = int(A / 10)
	B = int(B / 10)
print(max(a, b))