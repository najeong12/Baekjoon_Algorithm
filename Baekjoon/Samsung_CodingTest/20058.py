import copy
import sys
sys.setrecursionlimit(10**5)

ice = []
L_list = []
def rotate_ice(ice_width, box_width):
    tmp = copy.deepcopy(ice)
    for i in range(0, ice_width, box_width):
        for j in range(0, ice_width, box_width):
            for r in range(box_width):
                for c in range(box_width):
                    ice[i+r][j+c] = tmp[i+box_width-1-c][j+r]

def melt_ice(dir, ice_width):
    tmp = copy.deepcopy(ice)
    for i in range(ice_width):
        for j in range(ice_width):
            cnt = 0
            for d in dir:
                if (0 <= i + d[0] < ice_width) and (0 <= j + d[1] < ice_width):
                    if tmp[i+d[0]][j+d[1]] > 0: cnt += 1
            if cnt < 3 and ice[i][j] > 0:
                ice[i][j] -= 1

def dfs(ice, dir, x, y, ice_width):
    ret = 1
    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if (0 <= nx < ice_width) and (0 <= ny < ice_width) and (ice[nx][ny] > 0):
            ice[nx][ny] = 0
            ret += dfs(ice, dir, nx, ny, ice_width)
    return ret

if __name__ == '__main__':
    # 입력받기
    N, Q = map(int, input().split())
    ice_width = 2**N
    for i in range(ice_width):
        ice.append(list(map(int, input().split())))
    L_list = list(map(int, input().split()))
    dir = [[-1,0], [1,0],[0, -1], [0, 1]]

    for L in L_list:
        # 회전하기
        rotate_ice(ice_width, 2**L)
        # 0 인 것이 0, 1, 2 개면 -1
        melt_ice(dir, ice_width)

        # print(" ")
        # for i in range(ice_width):
        #     print(ice[i])

    # 전체 얼음의 합
    sum_all = 0
    for i in range(ice_width):
        sum_all += sum(ice[i])

    print(sum_all)

    # 가장 큰 덩어리의 크기
    ans = 0
    for x in range(ice_width):
        for y in range(ice_width):
            if ice[x][y] > 0:
                ice[x][y] = 0
                ans = max(ans, dfs(ice, dir, x, y, ice_width))
    print(ans)