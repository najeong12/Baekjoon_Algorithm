import copy
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = []

def dfs(x, y, board, N, prev, value, visited):
	if x == N-1 and y == N-1:
		answer.append(value)
		return
	for i in range(0, 4):
		nx = x + dx[i]
		ny = y + dy[i]
		if (0 <= nx <= N-1 and 0 <= ny <= N-1 and board[nx][ny] == 0 and visited[nx][ny] == 0):
			visited[nx][ny] = 1
			if prev == 9:
				value = value + 100
			elif prev == i:
				value = value + 100
			elif prev != i:
				value = value + 600
			prev = i
			tmp = copy.deepcopy(visited)
			dfs(nx, ny, board, N, prev, value, tmp)

def solution(board):
	N = len(board)
	visited = [[0 for _ in range(N)] for _ in range(N)]
	visited[0][0] = 1
	dfs(0, 0, board, N, 9, 0, visited)
	return min(answer)


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
