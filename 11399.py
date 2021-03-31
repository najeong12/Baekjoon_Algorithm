N = int(input())
arr=list(map(int, input().split()))
arr.sort()
arr.reverse()

answer = 0
for i in range(N):
    for j in range(i, N):
        answer += arr[j]
print(answer)