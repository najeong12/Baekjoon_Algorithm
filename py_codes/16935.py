# 연산 1
def fun1(N, M, arr):
    tmp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        tmp[i] = arr[N-1-i]
    return tmp

# 연산 2
def fun2(N, M, arr):
    tmp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = arr[i][M-1-j]
    return tmp

# 연산 3
def fun3(N, M, arr):
    tmp = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            tmp[i][j] = arr[N-1-j][i]
    return tmp

# 연산 4
def fun4(N, M, arr):
    tmp = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            tmp[i][j] = arr[j][M-1-i]
    return tmp

# 연산 5
def fun5(N, M, arr):
    tmp = [[0 for _ in range(M)] for _ in range(N)]
    n = int(N/2)
    m = int(M/2)
    for i in range(N):
        for j in range(M):
            if (0 <= i < n and 0 <= j < m):
                tmp[i][j] = arr[i + n][j]
            elif (0 <= i < n and j >= m):
                tmp[i][j] = arr[i][j - m]
            elif (i >= n and j >= m):
                tmp[i][j] = arr[i-n][j]
            elif (i >= n and 0 <= j < m):
                tmp[i][j] = arr[i][j+m]
    return tmp

# 연산 6
def fun6(N, M, arr):
    tmp = [[0 for _ in range(M)] for _ in range(N)]
    n = int(N/2)
    m = int(M/2)
    for i in range(N):
        for j in range(M):
            if (0 <= i < n and 0 <= j < m):
                tmp[i][j] = arr[i][j+m]
            elif (0 <= i < n and j >= m):
                tmp[i][j] = arr[i+n][j]
            elif (i >= n and j >= m):
                tmp[i][j] = arr[i][j-m]
            elif (i >= n and 0 <= j < m):
                tmp[i][j] = arr[i-n][j]
    return tmp

# 입력받기
N, M, R = map(int , input().split())
arr=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
fun = list(map(int, input().split()))

# 연산하기
for i in fun:
    if i == 1:
        arr = fun1(N, M, arr)
    elif i == 2:
        arr = fun2(N, M, arr)
    elif i == 3:
        arr = fun3(N, M, arr)
        tmp = N
        N = M
        M = tmp
    elif i == 4:
        arr = fun4(N, M, arr)
        tmp = N
        N = M
        M = tmp
    elif i == 5:
        arr = fun5(N, M, arr)
    elif i == 6:
        arr = fun6(N, M, arr)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end = " ")
    print("")