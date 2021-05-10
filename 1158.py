N, K = map(int, input().split())
visited = [0 for _ in range(N+1)]
answer = []

num = K
answer.append(num)
visited[num] = 1
while len(answer) < N:
    cycle = 0
    while cycle < K:
        num = 1 if num == N else num+1
        if visited[num] == 0:
            cycle += 1
    answer.append(num)
    visited[num] = 1

print("<", end="")
for i in range(N):
    if i != N-1:
        print(answer[i], end="")
        print(", ", end="")
    else:
        print(answer[i], end="")
print(">", end="")