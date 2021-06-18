import copy

N, M = map(int, input().split())
shark = []
for i in range(N):
    shark.append(list(map(int, input().split())))

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(x, y):
    global shark, N, M
    shark2 = copy.deepcopy(shark)
    if shark2[x][y] == 1:
        return 0
    safe = [0]
    arr = [[x, y]]
    shark2[x][y] = 2
    while len(safe) > 0:
        _safe = safe[0]
        safe.remove(_safe)
        _arr = arr[0]
        arr.remove(_arr)
        for k in range(8):
            nx = _arr[0] + dx[k]
            ny = _arr[1] + dy[k]
            if (0 <= nx < N) and (0 <= ny < M) and shark2[nx][ny] != 2:
                if shark2[nx][ny] == 1:
                    return _safe + 1
                else:
                    arr.append([nx, ny])
                    safe.append(_safe+1)
                    shark2[nx][ny] = 2


    return max(N, M)

MAX = 0
for i in range(N):
    for j in range(M):
        MAX = max(MAX, bfs(i, j))

print(MAX)