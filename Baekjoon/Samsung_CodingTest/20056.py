marble = []

# 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
def move_marble(visited, N):
    for arr in marble:
        _r = arr[0]
        _c = arr[1]
        _s = arr[3]
        _d = arr[4]
        visited[_r][_c].remove(arr)
        _r = ((_r + dr[_d] * _s) + N) % N
        _c = ((_c + dc[_d] * _s) + N) % N
        if _r == 0:
            _r = N
        if _c == 0:
            _c = N
        arr[0] = _r
        arr[1] = _c
        arr[3] = _s
        arr[4] = _d
        visited[_r][_c].append(arr)

    return visited

if __name__ == '__main__':
    marble = []
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]

    # N, M, K, marble 입력받기
    N, M, K = map(int, input().split())
    visited = [[[] for _ in range(N+1)] for _ in range(N+1)]

    for i in range(M):
        arr = list(map(int, input().split()))
        marble.append(arr)
        visited[arr[0]][arr[1]].append(arr)

    while K > 0:
        K -= 1
        visited = move_marble(visited, N)
        # marble 배열 row, column 순서로 정렬
        marble = sorted(marble, key=lambda x: (x[0], x[1]))
        ## 같은 칸에 두개 이상의 구슬이 있으면 4개로 쪼개기
        for i in range(1, N+1):
            for j in range(1, N+1):
                if len(visited[i][j]) >= 2:
                    dd = []
                    sum_m = 0
                    sum_s = 0
                    num = len(visited[i][j])
                    for nn in range(num):
                        arr2 = visited[i][j][0]
                        sum_m += arr2[2]
                        sum_s += arr2[3]
                        if (arr2[4] % 2) == 0:
                            dd.append(0)
                        else:
                            dd.append(1)
                        marble.remove(arr2)
                        visited[i][j].remove(arr2)
                    mm = sum_m//5
                    ss = sum_s//num
                    if mm != 0:
                        if (dd.count(1) == num) or (dd.count(0) == num):
                            for k in range(4):
                                new_arr = [i, j, mm, ss, 2*k]
                                marble.append(new_arr)
                                visited[i][j].append(new_arr)
                        else:
                            for k in range(4):
                                new_arr = [i, j, mm, ss, 2*(k+1) - 1]
                                marble.append(new_arr)
                                visited[i][j].append(new_arr)

    ## 질량의 합 구하기
    result = 0
    for arr in marble:
        result += arr[2]

    print(result)