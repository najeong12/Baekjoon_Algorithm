def sum_i2j(i, j, arr):
    answer = 0
    for k in range(i, j+1):
        answer += arr[k]
    return answer

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
result = 0

while (start < N and end < N):
    if (sum_i2j(start, end, arr) == M):
        result += 1
        end += 1
    elif (sum_i2j(start, end, arr) < M):
        end += 1
    elif (sum_i2j(start, end, arr) > M):
        if start == end:
            end += 1
        else:
            start += 1
    
print(result)