# 배열 사각형 1개 1바퀴 돌리기
def Rotate_Square(i, N, M, arr):
    saero = N - i
    garo = M - i
    start = i
    temp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(0, N):
        for j in range(0, M):
            temp = move_point(i, j, start, saero, garo, arr, temp)
    return temp

# arr 배열의 i, j 번째를 temp 배열에 돌려서 저장
def move_point(i, j, start, saero, garo, arr, temp):
    if (i == start and start < j <= garo - 1):        # 1
        temp[i][j-1] = arr[i][j]
    elif (start <= i < saero - 1 and j == start):     # 2
        temp[i+1][j] = arr[i][j]
    elif (i == saero - 1 and start <= j < garo - 1):  # 3
        temp[i][j+1] = arr[i][j]
    elif (start < i <= saero - 1 and j == garo - 1):  # 4
        temp[i-1][j] = arr[i][j]
    else:                                             # 5
        temp[i][j] = arr[i][j]
    return temp

# 배열 최종 출력
def my_print(arr):
    for i in range(N):
        for j in range(M):
            print(arr[i][j], "", end = "")
        print()

N, M, R = map(int, input().split())
arr =[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split())) # arr 입력받기

square_num = min(N, M) // 2 # 사각형의 개수
rotate_num = R % 2*(N+M-2)  # 회전하는 수 (4*4 사각형이면 2번 도는 것고 14번 도는 것이 같음!)
for _ in range(R):
    for i in range(square_num):
        arr = Rotate_Square(i, N, M, arr)

my_print(arr)