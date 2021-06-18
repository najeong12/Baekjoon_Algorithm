N, M = map(int, input().split())
tree=list(map(int, input().split()))
tree.sort()

left = 0
right = 0
for i in range(N):
    if right < tree[i]:
        right = tree[i]

while (left <= right):
    mid = (left + right) // 2
    cut = 0
    for i in range(N):
        if (tree[i] >= mid):
            cut += tree[i] - mid
    if cut >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)